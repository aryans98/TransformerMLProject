import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the data
data = pd.read_csv("data/transformer_data.csv")

# Features (X) and target (y) columns
features = ["Voltage Rating (kV)", "Current Rating (A)", "Power Rating (kVA)",
            "Efficiency (%)", "Temperature (°C)", "Weight (kg)",
            "Cost ($)", "Noise Level (dB)", "Reliability (years)"]

X = data[features]
y = data["Transformer Name"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Classifier and train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model to a file
joblib.dump(model, "models/transformer_model.pkl")
print("Trained model has been saved to 'models/transformer_model.pkl'.")
