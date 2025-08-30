# 🏦 Loan Prediction App
link : https://miniprojectdataengineering-loan-pratik.streamlit.app/

This project is an **end-to-end Data Engineering & Machine Learning pipeline** that predicts **Loan Approval Status**.  
The workflow involves **loading JSON data into MySQL**, training a classification model in Python, saving the model as a `.pickle` file, and finally deploying it as a **Streamlit web app**.

---

## 📌 Project Workflow

1. **Data Preparation**
   - Split the dataset into **three JSON files**:  
     - `applicant_info.json` → Applicant details  
     - `financial_info.json` → Financial details  
     - `loan_info.json` → Loan details  

2. **Database Storage**
   - Loaded JSON files into **MySQL database (`loan_db`)** using Python.

3. **Machine Learning**
   - Fetched data from MySQL into Python.
   - Performed preprocessing (encoding, scaling).
   - Trained a **RandomForestClassifier** model.
   - Saved the trained model and scaler as `.pkl` files.

4. **Streamlit Deployment**
   - Built a user-friendly **Streamlit app** (`app.py`) that:
     - Takes input from users.
     - Applies the same preprocessing.
     - Loads the saved model.
     - Predicts **Loan Approval Status** (Approved / Rejected).

---

## 🔄 Workflow Diagram

```mermaid
flowchart LR
    A[📂 JSON Files] -->|Load with Python| B[(🗄️ MySQL Database)]
    B -->|Fetch Data| C[⚙️ Python Preprocessing]
    C --> D[🤖 ML Model Training]
    D -->|Save| E[(📦 model.pkl & scaler.pkl)]
    E -->|Use in| F[🌐 Streamlit App]
    F -->|Predict| G[✅ Loan Status]
