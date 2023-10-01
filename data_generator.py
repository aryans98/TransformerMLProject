import pandas as pd
import random
import string

# Function to generate random string for transformer names
def generate_random_name():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(8))

# Function to generate transformer data
def generate_transformer_data(num_transformers):
    transformer_data = []

    for _ in range(num_transformers):
        transformer_name = generate_random_name()
        voltage_rating = random.uniform(5, 50)
        current_rating = random.uniform(10, 200)
        power_rating = voltage_rating * current_rating
        efficiency = random.uniform(80, 99)
        temperature = random.uniform(25, 90)
        weight = random.uniform(100, 2000)
        cost = random.uniform(1000, 5000)
        noise_level = random.uniform(50, 80)
        reliability = random.uniform(5, 30)

        transformer_data.append([transformer_name, voltage_rating, current_rating, power_rating, efficiency,
                                 temperature, weight, cost, noise_level, reliability])

    columns = ['Transformer Name', 'Voltage Rating (kV)', 'Current Rating (A)', 'Power Rating (kVA)',
               'Efficiency (%)', 'Temperature (°C)', 'Weight (kg)', 'Cost ($)', 'Noise Level (dB)',
               'Reliability (years)']

    data_frame = pd.DataFrame(transformer_data, columns=columns)
    return data_frame

# Main function to handle user input and generate data
if __name__ == "__main__":
    num_transformers = int(input("Enter the number of transformers to generate: "))
    
    if num_transformers <= 0:
        print("Invalid input. Please enter a positive number of transformers.")
    else:
        transformer_data = generate_transformer_data(num_transformers)
        transformer_data.to_csv('data/transformer_data.csv', index=False)
        print(f'{num_transformers} transformers data has been generated and saved to "data/transformer_data.csv".')
