from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import os
import logging
import instaloader
import numpy as np
import joblib
from datetime import datetime, timedelta

app = Flask(__name__, static_folder='../virtualr-main/dist', static_url_path='/')
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://localhost:3001"]}})

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this!
jwt = JWTManager(app)

# Configure MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
users_collection = db['users']

logging.basicConfig(level=logging.DEBUG)

# Load the model
model = joblib.load(r'D:\virtualr-main\Backend\mlp_model1.pkl')

@app.route('/')
def serve():
    app.logger.info("Serving React index.html")
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/health', methods=['GET'])
def health_check():
    app.logger.info("Health check endpoint called")
    return jsonify({"status": "Backend is running"}), 200

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    insta_user = data.get('insta_user')

    if not all([name, email, password, insta_user]):
        return jsonify({'error': 'All fields are required'}), 400

    if users_collection.find_one({'email': email}):
        return jsonify({'error': 'Email already exists'}), 400

    hashed_password = generate_password_hash(password)
    user = {
        'name': name,
        'email': email,
        'password': hashed_password,
        'insta_user': insta_user
    }
    users_collection.insert_one(user)

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = users_collection.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=str(user['_id']))
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/analyze/account', methods=['POST'])
@jwt_required()
def analyze_account():
    app.logger.info("Analyze account endpoint called")
    data = request.json
    profile_link = data.get('profile_link')
    
    if not profile_link:
        app.logger.error("No profile link provided")
        return jsonify({'error': 'No profile link provided'}), 400
    
    try:
        username = extract_username(profile_link)
        features, account_stats, recent_posts = fetch_user_data(username)
        
        if features is None:
            return jsonify({'error': 'Unable to fetch user data'}), 400
        
        features_2d = np.array([list(features.values())])
        prediction = model.predict_proba(features_2d)[:, 1]
        
        result = {
            "prediction": float(prediction[0]),
            "message": f"The possibility of the account being fake is {prediction[0]:.2%}",
            "accountStats": account_stats,
            "recentPosts": recent_posts
        }
        
        app.logger.info(f"Analysis Result: {result}")
        app.logger.info("Analysis completed successfully")
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"Error during analysis: {e}")
        return jsonify({'error': 'An error occurred during analysis'}), 500

def fetch_user_data(username):
    L = instaloader.Instaloader()
    L.load_session_from_file('ash_cartel52')
    if not L.context.is_logged_in:
        L.context.login('ash_cartel52', 'ADITYA@4555')

    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except instaloader.exceptions.ProfileNotExistsException:
        return None, None, None

    num_numeric_chars = sum(c.isdigit() for c in username)
    total_length = len(username)
    nums_length_ratio = num_numeric_chars / total_length if total_length > 0 else 0
    full_name_words = len(profile.full_name.split())

    features = {
        'Profile Pic': 1 if profile.profile_pic_url else 0,
        'Nums/Length Username': nums_length_ratio,
        'Full Name Words': full_name_words,
        'Bio Length': len(profile.biography),
        'External Url': 1 if profile.external_url else 0,
        'Verified': 1 if profile.is_verified else 0,
        'Business': 1 if profile.is_business_account else 0,
        '#Posts': profile.mediacount,
        '#Followers': profile.followers,
        '#Following': profile.followees,
    }

    account_stats = {
        'posts': profile.mediacount,
        'followers': profile.followers,
        'following': profile.followees
    }

    recent_posts = []
    for post in profile.get_posts():
        recent_posts.append({
            'likes': post.likes,
            'comments': post.comments
        })
        if len(recent_posts) >= 10:  # Limit to 10 recent posts
            break

    return features, account_stats, recent_posts

def extract_username(profile_link):
    username_with_slash = profile_link.rsplit('instagram.com/', 1)[-1]
    return username_with_slash[:-1] if username_with_slash.endswith('/') else username_with_slash

if __name__ == '__main__':
    app.run(debug=True, port=3001)