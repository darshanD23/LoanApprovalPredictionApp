import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open(r'C:\Users\DN10\Downloads\LOAN_APP\loan_model.pkl', 'rb'))

# Streamlit UI
st.title("Loan Approval Prediction App")
st.write("Enter the applicant's details to predict loan approval status:")

# Input fields
no_of_dependents = st.number_input("Number of Dependents", min_value=0, value=0)
education = st.selectbox("Education Level", ["Graduate", "Non-Graduate"])
self_employed = st.selectbox("Self-Employed", ["Yes", "No"])
income_annum = st.number_input("Annual Income (in INR)", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (in years)", min_value=0)
cibil_score = st.number_input("CIBIL Score", min_value=0)
residential_assets_value = st.number_input("Residential Assets Value", min_value=0)
commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0)
luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0)

# Encode categorical features
education_num = 1 if education == "Graduate" else 0
self_employed_num = 1 if self_employed == "Yes" else 0

# Prepare the input data
input_data = pd.DataFrame({
    'no_of_dependents': [no_of_dependents],
    'education': [education_num],
    'self_employed': [self_employed_num],
    'income_annum': [income_annum],
    'loan_amount': [loan_amount],
    'loan_term': [loan_term],
    'cibil_score': [cibil_score],
    'residential_assets_value': [residential_assets_value],
    'commercial_assets_value': [commercial_assets_value],
    'luxury_assets_value': [luxury_assets_value],
    'bank_asset_value': [bank_asset_value]
})

# Predict using the loaded model
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Congratulations! The loan is APPROVED ✅")
    else:
        st.error("Sorry, the loan is REJECTED ❌")
