from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)  # correct


# Load the trained model
model = joblib.load('house_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from form
    square_footage = float(request.form['square_footage'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    
    # Prepare input data for prediction
    input_data = pd.DataFrame([[square_footage, bedrooms, bathrooms]], columns=['SquareFootage', 'Bedrooms', 'Bathrooms'])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction:.2f}')

if __name__ == "__main__":
    app.run(debug=True)