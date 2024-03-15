import json
import numpy as np
import pandas as pd
import pickle

def compare_transformers():
    # Load the input data
    v = float(input("Enter v: "))
    u = float(input("Enter u: "))
    f = float(input("Enter f: "))
    h = float(input("Enter h: "))
    
    input_data = {'v': v, 'u': u, 'f': f, 'h': h}
    
    # Load the trained model
    with open('transformer_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    
    # Load transformer data
    with open('transformer_data.json', 'r') as json_file:
        transformer_data = json.load(json_file)
    
    # Create a DataFrame for input data
    input_df = pd.DataFrame(input_data, index=[0])
    
    # Predict rankings for all transformers
    rankings = {}
    for transformer in transformer_data:
        transformer_name = transformer['name']
        transformer_features = list(transformer['features'].values())
        transformer_features_encoded = np.array(transformer_features).reshape(1, -1)
        
        # Predict the ranking
        ranking = model.predict(transformer_features_encoded)[0]
        
        rankings[transformer_name] = ranking
    
    # Sort transformers based on their predicted rankings
    sorted_rankings = sorted(rankings.items(), key=lambda x: x[1])
    
    # Print the rankings
    print("\nTransformer Rankings based on the given data:")
    for rank, (transformer, ranking) in enumerate(sorted_rankings, start=1):
        print(f"Rank {rank}: {ranking} ({transformer})")

if __name__ == "__main__":
    compare_transformers()

# a, b, c, d, e, f, g, h, i, j