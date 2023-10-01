import pandas as pd
import random

# Function to generate simulated data for transformers
def generate_transformer_data(num_transformers):
    transformer_data = []
    transformer_names = ["Transformer A", "Transformer B", "Transformer C", "Transformer D", "Transformer E"]

    for _ in range(num_transformers):
        transformer = {
            "Transformer Name": random.choice(transformer_names),
            "Voltage Rating (kV)": round(random.uniform(10, 50), 2),
            "Current Rating (A)": round(random.uniform(50, 500), 2),
            "Power Rating (kVA)": round(random.uniform(50, 1000), 2),
            "Efficiency (%)": round(random.uniform(90, 98), 2),
            "Temperature (°C)": round(random.uniform(25, 90), 2),
            "Weight (kg)": round(random.uniform(500, 5000), 2),
            "Cost ($)": round(random.uniform(1000, 50000), 2),
            "Noise Level (dB)": round(random.uniform(50, 80), 2),
            "Reliability (years)": round(random.uniform(10, 30), 2)
        }
        transformer_data.append(transformer)

    # Create a DataFrame from the generated data
    df = pd.DataFrame(transformer_data)
    return df

# Main function to generate data and save it to a CSV file
if __name__ == "__main__":
    num_transformers = int(input("Enter the number of transformers to generate data for: "))
    data = generate_transformer_data(num_transformers)
    data.to_csv("data/transformer_data.csv", index=False)
    print(f"Simulated data for {num_transformers} transformers has been generated and saved to 'data/transformer_data.csv'.")
