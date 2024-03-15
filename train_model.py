import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Step 1: Load the data from JSON file
with open('transformer_data.json', 'r') as file:
    data = json.load(file)

# Convert the data to a DataFrame
features = []
target = []
for item in data:
    features.append(item['features'])
    target.append(item['name'])

df = pd.DataFrame(features)
df['Transformer'] = target

# Step 2: Split the data into features (X) and target (y)
X = df.drop(columns=['Transformer'])
y = df['Transformer']

# Step 3: Split the data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Make predictions on the validation set
y_pred = model.predict(X_valid)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_valid, y_pred)
print(f'Validation Accuracy: {accuracy}')

# Step 7: Save the trained model
with open('transformer_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print('Model saved as transformer_model.pkl')
