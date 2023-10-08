import json
import random

def collect_transformer_data():
    num_transformers = int(input("Enter the number of transformers: "))
    features = input("Enter the names of features (comma-separated): ").split(',')

    transformers_data = []
    for i in range(num_transformers):
        transformer = {}
        transformer['name'] = f'Transformer-{i + 1}-{random.randint(100, 999)}'
        transformer['features'] = {}

        print(f"\nEnter data for {transformer['name']}:")
        for feature in features:
            value = input(f"Enter {feature}: ")
            transformer['features'][feature.strip()] = value

        transformers_data.append(transformer)

    with open('transformer_data.json', 'w') as outfile:
        json.dump(transformers_data, outfile, indent=4)

if __name__ == "__main__":
    collect_transformer_data()
