# Transformer Analysis Project

This project simulates data for different transformers and uses a machine learning model to determine which transformer is better based on various features.

## Project Structure

- `data/`: Contains the simulated data for transformers.
- `models/`: Contains the machine learning model.
- `app.py`: Main Python script for user input and evaluation.
- `data_generator.py`: Script to generate simulated transformer data.
- `models/model.py`: Script to build and train the machine learning model.
- `requirements.txt`: List of project dependencies.
- `README.md`: Project documentation (you're reading it!).

## Instructions

1. **Generate Simulated Data:**
   Run `python data_generator.py` to generate simulated transformer data. The data will be saved in `data/transformer_data.csv`.

2. **Train the Machine Learning Model:**
   Run `python models/model.py` to train the machine learning model using the generated data. The trained model will be saved in `models/transformer_model.pkl`.

3. **Evaluate Transformers:**
   Run `python app.py` to input features for a transformer and see the prediction from the trained model.

4. **Deployment:**
   - The code is hosted on GitHub: [GitHub Repository](https://github.com/aryans98/TransformerMLProject).

## Technologies Used

- Python
- Pandas
- scikit-learn
- GitHub (for version control)

Feel free to explore the code and adapt it for your own use!