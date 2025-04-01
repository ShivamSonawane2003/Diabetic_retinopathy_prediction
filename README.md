# Diabetic retinopathy prediction in patients 

## 📌 Overview
This project aims to predict whether a patient has diabetic retinopathy using machine learning. It is a **binary classification** problem, where the target variable has two values: 
- **0** (No Retinopathy)
- **1** (Retinopathy Present)

The model is trained using patient health data, including blood pressure, cholesterol levels, and age.

## 📂 Dataset Details
The dataset consists of **6000 rows** and **6 columns**, including:
1. **ID**: Unique identifier for each patient.
2. **Age**: Patient's age (numeric).
3. **Systolic BP**: Systolic blood pressure (normal range: below 120mmHg).
4. **Diastolic BP**: Diastolic blood pressure (normal range: below 80mmHg).
5. **Cholesterol**: Cholesterol levels (normal range: 125-200 mg/dL).
6. **Prognosis**: Target variable (0 or 1).

## 🚀 Tools & Technologies
- **Python** (NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn)
- **Jupyter Notebook** for development
- **Machine Learning Models** (Logistic Regression, Decision Trees, Random Forest, etc.)
- **Deployment Framework**: Streamlit
- **Version Control**: Git & GitHub

## ⚙️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/ShivamSonawane2003/diabetic-retinopathy.git
   ```
2. Navigate to the project directory:
   ```bash
   cd diabetic-retinopathy
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter Notebook:
   ```bash
    Diabetic_retinopathy.ipynb
   ```
5. For deployment, run:
   ```bash
   streamlit run Diabetic_retinopathy.py
   ```
