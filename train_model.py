import json
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.preprocessing import LabelEncoder

def train_model():
    with open('transformer_data.json', 'r') as infile:
        data = json.load(infile)

    features = list(data[0]['features'].keys())
    X = [[float(transformer['features'][feature]) for feature in features] for transformer in data]
    transformer_names = [transformer['name'] for transformer in data]

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(transformer_names)

    model = RandomForestClassifier()
    model.fit(X, y)

    with open('transformer_model.pkl', 'wb') as model_file:
        pickle.dump((model, label_encoder), model_file)

if __name__ == "__main__":
    train_model()
