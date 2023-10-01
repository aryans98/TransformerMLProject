import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/transformer_model.pkl")

# Function to get user input and make predictions
def predict_transformer():
    features = ["Voltage Rating (kV)", "Current Rating (A)", "Power Rating (kVA)",
                "Efficiency (%)", "Temperature (°C)", "Weight (kg)",
                "Cost ($)", "Noise Level (dB)", "Reliability (years)"]

    user_data = []
    for feature in features:
        value = float(input(f"Enter {feature}: "))
        user_data.append(value)

    # Make a prediction using the trained model
    prediction = model.predict([user_data])
    print(f"The predicted transformer for the given features is: {prediction[0]}")

# Main function to handle user input and prediction
if __name__ == "__main__":
    print("Enter the features for the transformer:")
    predict_transformer()
