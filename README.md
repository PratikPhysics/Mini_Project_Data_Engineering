# 🏦 Loan Prediction App

This project is an **end-to-end Data Engineering & Machine Learning pipeline** that predicts **Loan Approval Status**.  
The workflow involves **loading JSON data into MySQL**, training a classification model in Python, saving the model as a `.pickle` file, and finally deploying it as a **Streamlit web app**.  

---

## 📌 Project Workflow

1. **Data Preparation**
   - Started with a CSV file containing loan applicant data.  
   - Split the data into **three JSON files**:  
     - `applicant_info.json` → Applicant details (Gender, Education, Dependents, etc.)  
     - `financial_info.json` → Financial details (Income, Loan Amount, Credit History, etc.)  
     - `loan_info.json` → Loan details (Property Area, Loan Status)  

2. **Database Storage**
   - Loaded the JSON files into **MySQL** using Python (`pymysql` + `pandas`).  
   - Created a new database **`loan_db`** and stored each JSON as a table:  
     - `applicant_info`  
     - `financial_info`  
     - `loan_info`  

3. **Machine Learning**
   - Loaded the data back from MySQL into Python.  
   - Preprocessed the dataset (handled categorical values, scaling numerical features).  
   - Trained a **classification model** (`RandomForestClassifier`) using **scikit-learn**.  
   - Saved the trained model and scaler as `.pickle` files (`model.pkl`, `scaler.pkl`).  

4. **Streamlit Deployment**
   - Built a simple **Streamlit app (`app.py`)** that:  
     - Accepts applicant input through a form.  
     - Applies the same preprocessing (encoding + scaling).  
     - Uses the trained ML model (`model.pkl`) to predict **Loan Approval Status**.  
   - Deployed the app on **Streamlit Cloud**.  

---

## 🚀 Live Demo
🔗 [Streamlit App](https://miniprojectdataengineering-loan-pratik.streamlit.app/)  

---

