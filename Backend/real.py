import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

# Load the dataset
df = pd.read_csv(r"D:\model_with_flask\transactions.csv")

# Handle missing values (if needed)
# df.fillna(method='ffill', inplace=True) # Example of handling missing values

# Label encode the 'Status' column
label_encoder = LabelEncoder()
df['Status'] = label_encoder.fit_transform(df['Status'])

# One-hot encode categorical columns
data_encoded = pd.get_dummies(df, columns=['Sender Name', 'Sender UPI ID', 'Receiver Name', 'Receiver UPI ID'])

# Convert the 'Timestamp' column to datetime format and extract features
data_encoded['Timestamp'] = pd.to_datetime(data_encoded['Timestamp'])
data_encoded['DayOfWeek'] = data_encoded['Timestamp'].dt.dayofweek
data_encoded['HourOfDay'] = data_encoded['Timestamp'].dt.hour

# Drop columns no longer needed
data_encoded.drop(columns=['Timestamp', 'Transaction ID'], inplace=True)

# Split the dataset into features and target variable
X = data_encoded.drop(columns=['Status'])
y = data_encoded['Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)
y_pred = rf_classifier.predict(X_test)

# Evaluate the initial model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Initial Model Accuracy: {accuracy}')
print(f'Initial Model Classification Report:\n{report}')

# Perform Grid Search for hyperparameter tuning
param_grid_rf = {
    'n_estimators': [100, 200, 300, 400, 500],
    'max_depth': [None, 10, 20, 30, 40],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search_rf = GridSearchCV(estimator=RandomForestClassifier(random_state=42), param_grid=param_grid_rf, cv=3, n_jobs=-1, verbose=2)
grid_search_rf.fit(X_train, y_train)

# Get best parameters and evaluate the tuned model
best_params_rf = grid_search_rf.best_params_
print(f'Best Parameters for Random Forest: {best_params_rf}')

best_model_rf = grid_search_rf.best_estimator_
y_pred_rf_tuned = best_model_rf.predict(X_test)
accuracy_rf_tuned = accuracy_score(y_test, y_pred_rf_tuned)
report_rf_tuned = classification_report(y_test, y_pred_rf_tuned)

print(f'Tuned Random Forest Accuracy: {accuracy_rf_tuned}')
print(f'Tuned Random Forest Classification Report:\n{report_rf_tuned}')

# Save the best model to a pickle file
with open('modelfinal.pickle', 'wb') as f:
    pickle.dump(best_model_rf, f)

with open('columns.pkl', 'wb') as f:
    pickle.dump(X.columns.tolist(), f)
# Load the model from the pickle file
with open('modelfinal.pickle', 'rb') as f:
    model = pickle.load(f)

# Test the loaded model (example)
# Make sure the new data has the same structure and features as the training data
