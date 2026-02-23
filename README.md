# Heart Disease Prediction using Machine Learning

This repository contains a Machine Learning project that predicts the 10-year risk of coronary heart disease (CHD) 
based on clinical and behavioral data. The project demonstrates a complete ML pipeline including preprocessing, 
scaling, model training, and a web-based deployment using Streamlit.

---

## Project Overview
Heart disease prediction is a critical application of Machine Learning in healthcare analytics. 
In this project, a Logistic Regression model is used to predict patient risk by learning patterns from the Framingham Heart Study dataset.

The trained model and preprocessing components are saved and reused for making real-time predictions through a Streamlit web application.

---

## Dataset
- Framingham Heart Study dataset (framingham_heart_disease.csv)
- Includes variables such as age, sex, BMI, cholesterol levels, cigarette consumption, and blood pressure.
- Target : 10-year risk of Coronary Heart Disease (CHD).

---

## Methodology
1. Data loading and exploration
2. Data preprocessing and cleaning
3. Feature scaling (Standardization)
4. Model training (Logistic Regression)
5. Model evaluation
6. Model serialization for deployment

---

## Machine Learning Components
- Trained Prediction Model (`logistic_model.pkl`)
- Feature Scaler (`scaler.pkl`)
- Web App Interface (`app.py`)

---

## Results
The Logistic Regression model provides a probability-based classification, allowing the app to determine 
if a patient is at high risk based on their clinical profile with reliable accuracy.

---

## How to Run

1. Clone the repository
2. Install required libraries:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   streamlit run app.py
   ```

---

## Technologies Used
- Python
- Pandas & NumPy 
- Scikit-learn 
- Streamlit 
- Pickle

---

## Academic Purpose
This project is developed as part of Machine Learning coursework to demonstrate 
end-to-end model development, preprocessing, and deployment using a real-world healthcare datas

---

## Repository Structure
