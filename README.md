# 🏦 Loan Prediction App

This project is an **end-to-end data engineering & machine learning pipeline** for predicting loan approvals.  
The app is deployed on **Streamlit** and connected to a **MySQL database** for data storage.

---

## 📌 Project Overview
- Extracted data from CSV → converted into JSON.  
- Stored applicant, financial, and loan data in **MySQL** using Python.  
- Preprocessed and cleaned data for ML training.  
- Trained a **classification model** (RandomForestClassifier) using scikit-learn.  
- Saved the model with **pickle** for deployment.  
- Built a **Streamlit web app** for interactive predictions.  
- Deployed app on **Streamlit Cloud** and hosted project on GitHub.

---

## 🚀 Live Demo
🔗 [Streamlit App](https://miniprojectdataengineering-loan-pratik.streamlit.app/)  

---

## 📂 Project Structure
├── app.py # Streamlit application
├── train_model.py # ML training script
├── load_data_mysql.py # Script to load data into MySQL
├── applicant_info.json # Applicant dataset
├── financial_info.json # Financial dataset
├── loan_info.json # Loan dataset
├── model.pkl # Trained ML model
├── scaler.pkl # Scaler for preprocessing
├── requirements.txt # Dependencies
└── README.md # Project documentation
