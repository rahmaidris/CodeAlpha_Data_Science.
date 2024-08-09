# Titanic Survival Prediction

## Overview

This project is a web application for predicting survival outcomes on the Titanic using a Flask backend. It takes user input regarding passenger details and provides a prediction on whether the passenger would have survived the disaster. The application uses a machine learning model trained on Titanic dataset features.

## Project Structure

- **`app.py`**: Flask application that handles form submission, makes predictions, and displays results.
- **`model.pkl`**: Serialized machine learning model used for making predictions.
- **`index.html`**: HTML file for the user input form.
- **`result.html`**: HTML file to display prediction results.
- **`notebook.ipynb`**: Jupyter notebook containing exploratory data analysis and model training.

## Screenshots

### Input Form

![Input Form](assets/input_form.png)

### Prediction Results

![Prediction Results](assets/prediction_results.png)

## Getting Started

### Prerequisites

Ensure you have Python and the following packages installed:
- Flask
- scikit-learn
- joblib

You can install these packages using pip:

```bash
pip install Flask scikit-learn joblib
