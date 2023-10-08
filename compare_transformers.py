import json
import pickle
import pandas as pd

def get_user_input(features):
    user_data = {}
    print("Enter data for comparison:")
    for feature in features:
        value = input(f"Enter {feature}: ")
        user_data[feature] = float(value)  # Convert user input to float
    return user_data

def compare_transformers():
    with open('transformer_data.json', 'r') as infile:
        data = json.load(infile)

    features = list(data[0]['features'].keys())

    # Get user input for comparison
    user_data = get_user_input(features)

    with open('transformer_model.pkl', 'rb') as model_file:
        model, label_encoder = pickle.load(model_file)

    # Prepare user input for prediction
    input_data = [user_data[feature] for feature in features]
    input_data = [input_data]  # Model.predict() expects a 2D array

    predictions = model.predict(input_data)[0]

    # Predict scores for all transformers in the data
    transformer_features = [[transformer['features'][feature] for feature in features] for transformer in data]
    transformer_predictions = model.predict(transformer_features)
    
    # Create a DataFrame to hold transformer names and prediction scores
    transformer_names = [transformer['name'] for transformer in data]
    ranking_data = {'Transformer': transformer_names, 'Prediction': transformer_predictions}
    ranking_df = pd.DataFrame(ranking_data)
    
    # Sort the DataFrame based on prediction scores in descending order
    ranking_df = ranking_df.sort_values(by='Prediction', ascending=False).reset_index(drop=True)
    
    # Rank transformers from best to worst and print the ranking
    ranked_transformers = ranking_df.index + 1
    ranking_df['Rank'] = ranked_transformers
    
    print("\nTransformer Rankings based on the given data:")
    print(ranking_df)

if __name__ == "__main__":
    compare_transformers()
