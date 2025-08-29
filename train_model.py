# train_model.py
import pandas as pd
import pymysql
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

# ========== 1. Connect to MySQL and Load Data ==========
conn = pymysql.connect(
    host="localhost",
    user="root",          # 🔧 change if needed
    password="pratik",  # 🔧 change if needed
    database="loan_db"
)

df_applicant = pd.read_sql("SELECT * FROM applicant_info", conn)
df_financial = pd.read_sql("SELECT * FROM financial_info", conn)
df_loan = pd.read_sql("SELECT * FROM loan_info", conn)

conn.close()
print("✅ Data loaded from MySQL")

# ========== 2. Merge Data ==========
df = df_applicant.merge(df_financial, on="Loan_ID", how="inner")
df = df.merge(df_loan, on="Loan_ID", how="inner")

print("Merged Data Shape:", df.shape)

# ========== 3. Preprocessing ==========
# Drop Loan_ID (not useful for prediction)
df.drop(columns=["Loan_ID"], inplace=True)

# Encode categorical variables
cat_cols = df.select_dtypes(include=["object"]).columns
le = LabelEncoder()
for col in cat_cols:
    df[col] = df[col].astype(str)  # ensure string
    df[col] = le.fit_transform(df[col])

# Handle missing values (replace with mean for numeric, mode for categorical)
for col in df.columns:
    if df[col].dtype in [np.float64, np.int64]:
        df[col] = df[col].fillna(df[col].mean())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# Split features and target
X = df.drop(columns=["Loan_Status"])
y = df["Loan_Status"]

# Scale numeric values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ========== 4. Train/Test Split ==========
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# ========== 5. Train Model ==========
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# ========== 6. Evaluate ==========
y_pred = model.predict(X_test)

print("\n🎯 Model Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# ========== 7. Save Model with Pickle ==========
with open("loan_approval_model.pkl", "wb") as f:
    pickle.dump((model, scaler, le), f)

print("💾 Model saved as loan_approval_model.pkl")
