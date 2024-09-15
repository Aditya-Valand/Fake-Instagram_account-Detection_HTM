# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.feature_selection import SelectKBest, chi2
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, confusion_matrix
# from sklearn.model_selection import cross_val_score
# from sklearn.metrics import classification_report, confusion_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns

# # df = pd.read_csv(r"D:\model_with_flask\Dataset.csv", encoding='utf-8', errors='ignore')
# # import pandas as pd

# try:
#     df = pd.read_csv(r"D:\model_with_flask\dataset.csv", encoding='utf-8')
# except UnicodeDecodeError:
#     print("Error: Unable to decode file using UTF-8 encoding.")
#     # Handle the error here, such as trying a different encoding or skipping problematic lines.

# try:
#     X = df.drop('Fake', axis=1)
# except NameError:
#     print("Error: DataFrame 'df' is not defined.")
#     exit(1)  # Exit the script if an error occurs


# # Splitting the dataset into the Training set and Test set
# # X = df.drop('Fake', axis=1)
# y = df['Fake']

# # Splitting the dataset into the Training set and Test set
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# # Create a logistic regression model
# model = LogisticRegression()

# # Train the model

# from sklearn.preprocessing import StandardScaler

# # Scale the data
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Train the model using the scaled data
# model = LogisticRegression()
# model.fit(X_train, y_train)

# # Predict the test set
# from sklearn.model_selection import cross_val_score
# from sklearn.metrics import classification_report, confusion_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Assuming 'model' is your trained logistic regression model

# # Perform 5-fold cross-validation
# scores = cross_val_score(model, X_train, y_train, cv=5)

# # Calculate the mean accuracy of the model across all folds
# mean_accuracy = scores.mean()

# print(f'Mean accuracy of the model across 5-fold cross-validation: {mean_accuracy}')

# # Make predictions using the trained model
# predictions = model.predict(X_test)

# # Calculate the precision, recall, and F1-score of the model
# report = classification_report(y_test, predictions)

# print(report)

# # Visualize the confusion matrix
# cm = confusion_matrix(y_test, predictions)

# sns.heatmap(cm, annot=True, fmt='d')
# plt.title('Confusion Matrix')
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.show()
# import pickle

# # Assuming 'model' is your trained logistic regression model

# # Save the model to a file
# with open('model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# # Load the model from the file
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)    
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load the dataset
try:
    df = pd.read_csv(r"D:\model_with_flask\dataset.csv", encoding='utf-8')
except UnicodeDecodeError:
    print("Error: Unable to decode file using UTF-8 encoding.")
    exit(1)

# Prepare the feature matrix (X) and target vector (y)
X = df.drop('Fake', axis=1)
y = df['Fake']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a neural network classifier
model = MLPClassifier(hidden_layer_sizes=(100, 50), activation='relu', solver='adam', max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate the model
train_accuracy = model.score(X_train_scaled, y_train)
test_accuracy = model.score(X_test_scaled, y_test)
print(f'Training Accuracy: {train_accuracy:.4f}')
print(f'Test Accuracy: {test_accuracy:.4f}')

# Make predictions
predictions = model.predict(X_test_scaled)

# Generate evaluation metrics
print(classification_report(y_test, predictions))

# Visualize the confusion matrix
cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, fmt='d')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Save the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load the model from the file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
