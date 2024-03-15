import json
import pickle
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model():
    with open('transformer_data.json', 'r') as infile:
        data = json.load(infile)

    features = list(data[0]['features'].keys())
    X = [[float(transformer['features'][feature]) for feature in features] for transformer in data]
    transformer_names = [transformer['name'] for transformer in data]

    with open('transformer_model.pkl', 'rb') as model_file:
        model, label_encoder = pickle.load(model_file)

    y_true = label_encoder.transform(transformer_names)
    y_pred = model.predict(X)

    report = classification_report(y_true, y_pred)
    conf_matrix = confusion_matrix(y_true, y_pred)

    print("Classification Report:")
    print(report)
    print("\nConfusion Matrix:")
    print(conf_matrix)

if __name__ == "__main__":
    evaluate_model()
