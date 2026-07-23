# StaySure AI – Hotel Booking Cancellation Risk Predictor

Machine Learning for Developers (CAI2C08) Project

## Project Overview

StaySure AI is a machine learning web application that predicts whether a hotel booking is likely to be cancelled.

The project was developed using Python, scikit-learn and Streamlit. It uses historical hotel booking information to identify bookings that are at a higher risk of cancellation, enabling hotels to make more informed operational and reservation management decisions.

---

## Live Web Application

🔗 **[StaySure AI Streamlit App](https://staysure-ai-hotel-cancellation-lyakdrncnioqrh9uf3ryq8.streamlit.app)**

---

## Dataset

**Dataset:** Hotel Booking Cancellation Prediction

**Source:** [Kaggle - Hotel Booking Cancellation Prediction](https://www.kaggle.com/datasets/youssefaboelwafa/hotel-booking-cancellation-prediction)

---

## Machine Learning Task

**Problem Type:** Binary Classification

**Target Variable:**

`is_canceled`

Prediction values:

- **0** = Booking Not Cancelled
- **1** = Booking Cancelled

---

## Features Used

The final machine learning model uses the following features:

- Hotel
- Lead Time
- Deposit Type
- Market Segment
- Customer Type
- Total Nights
- Total Guests
- Has Children
- Has Special Request

---

## Final Machine Learning Model

The final deployed model is a tuned **Random Forest Classifier** developed using **scikit-learn**.

The model was selected after comparing multiple classification algorithms and evaluating their performance using the **F1-score**, making it the most suitable model for predicting hotel booking cancellations.

---

## Machine Learning Workflow

1. Data cleaning and preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature engineering
4. Model training and comparison
5. Hyperparameter tuning
6. Final model evaluation
7. Streamlit deployment

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- Streamlit
- Joblib
- GitHub

---

## Repository Structure

```
staysure-ai-hotel-cancellation/
│
├── data/
│   └── hotel_bookings.csv
│
├── models/
│   ├── tuned_random_forest_model.pkl
│   └── model_columns.pkl
│
├── notebooks/
│   └── staysure_model_development.ipynb
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Author

**Grishm Chandru Mirpuri**

Machine Learning for Developers (CAI2C08)

Diploma in Applied Artificial Intelligence

School of Informatics & IT

Temasek Polytechnic