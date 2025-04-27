# --- Import libraries
import streamlit as st
import pandas as pd
import pickle


# --- Load the trained model from the specified path
with open(r"C:\Users\Narula\Downloads\final_trained_model.pkl", "rb") as file:
    model = pickle.load(file)


# --- Streamlit App Title
st.title("💼 Data Science Salary Predictor")
st.subheader("📈 Estimate your salary based on your background and experience")

st.write("Please input your information below to predict your estimated yearly salary:")

# --- User Input Section

# Q11: Years of Coding
years_coding = st.selectbox(
    "How many years have you been coding?",
    ["I have never written code", "< 1 years", "1-3 years", "3-5 years", "5-10 years", "10-20 years", "20+ years"]
)

# Q16: Years of Machine Learning Experience
years_ml = st.selectbox(
    "How many years have you used machine learning methods?",
    ["I have never written code", "< 1 years", "1-3 years", "3-5 years", "5-10 years", "10-20 years", "20+ years"]
)

# Q26: Company Size
company_size = st.selectbox(
    "Size of your company?",
    ["0-49 employees", "50-249 employees", "250-999 employees", "1000-9,999 employees", "10,000 or more employees"]
)

# Q27: ML Usage at Employer
ml_usage = st.selectbox(
    "ML adoption at your employer?",
    [
        "No (we do not use ML methods)",
        "We are exploring ML methods (and may one day put a model into production)",
        "We recently started using ML methods (i.e., models in production)",
        "We use ML methods for generating insights (but models are not in production)",
        "We have well established ML methods (i.e., models in production for more than 2 years)"
    ]
)

# Q30: Spending on ML/Cloud Services
ml_spending = st.selectbox(
    "How much money have you spent on ML/Cloud services?",
    ["$0 ($USD)", "$1-$99", "$100-$999", "$1000-$9,999", "$10,000-$99,999", "$100,000 or more ($USD)"]
)

# --- Mapping user input to numeric values

years_mapping = {
    'I have never written code': 0,
    '< 1 years': 0.5,
    '1-3 years': 2,
    '3-5 years': 4,
    '5-10 years': 7.5,
    '10-20 years': 15,
    '20+ years': 25
}

company_mapping = {
    '0-49 employees': 25,
    '50-249 employees': 150,
    '250-999 employees': 625,
    '1000-9,999 employees': 5000,
    '10,000 or more employees': 15000
}

ml_use_mapping = {
    'No (we do not use ML methods)': 0,
    'We are exploring ML methods (and may one day put a model into production)': 1,
    'We recently started using ML methods (i.e., models in production)': 2,
    'We use ML methods for generating insights (but models are not in production)': 3,
    'We have well established ML methods (i.e., models in production for more than 2 years)': 4
}

ml_spending_mapping = {
    '$0 ($USD)': 0,
    '$1-$99': 50,
    '$100-$999': 550,
    '$1000-$9,999': 5000,
    '$10,000-$99,999': 55000,
    '$100,000 or more ($USD)': 150000
}

# Create the input DataFrame for prediction
input_data = pd.DataFrame([{
    "Years_Coding_Num": years_mapping[years_coding],
    "Years_ML_Num": years_mapping[years_ml],
    "Company_Size_Num": company_mapping[company_size],
    "ML_Use_Employer_Num": ml_use_mapping[ml_usage],
    "ML_Spending_Num": ml_spending_mapping[ml_spending]
}])

# --- Predict and Show Result

st.markdown("### 📊 Predicted Salary:")

if st.button("💵 Predict Salary"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Your estimated salary is: **${prediction:,.2f} per year**")

st.markdown("---")
st.markdown("<small>Built with ❤️ by [Your Name]</small>", unsafe_allow_html=True)
