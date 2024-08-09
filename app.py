from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    pclass = int(request.form['pclass'])
    sex = request.form['sex']
    age = float(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = float(request.form['fare'])
    embarked = request.form['embarked']

    # Convert categorical data to numerical values
    sex_male = 1 if sex == 'male' else 0
    embarked_s = 1 if embarked == 'S' else 0
    embarked_c = 1 if embarked == 'C' else 0
    embarked_q = 1 if embarked == 'Q' else 0

    # Create input array with 7 features
    features = np.array([[pclass, sex_male, age, sibsp, parch, fare, embarked_s]])

    # Make prediction
    prediction = model.predict(features)

    # Return result page with prediction
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
