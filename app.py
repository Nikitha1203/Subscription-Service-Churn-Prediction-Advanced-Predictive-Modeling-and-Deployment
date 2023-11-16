import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the trained model
model = joblib.load('customer_churn_model.joblib')

# Streamlit app
st.title("Customer Churn Prediction App")

# Add user input components
age = st.slider("Age", 18, 100, 25)
job = st.text_input("Job", "Engineer")
marital_status = st.selectbox("Marital Status", ["Single", "Married"])
education = st.selectbox("Education", ["PhD", "Master's", "Bachelor's", "High School"])
annual_income = st.number_input("Annual Income", min_value=0)
transaction_history = st.slider("Transaction History", 0, 20, 5)
payment_patterns = st.slider("Payment Patterns", 0, 10, 3)
service_usage_frequency = st.slider("Service Usage Frequency", 1, 30, 10)
service_usage_duration = st.slider("Service Usage Duration", 1, 50, 20)
most_used_features = st.selectbox("Most Used Features", ["A", "B", "C"])
support_interactions = st.slider("Support Interactions", 0, 5, 2)
feedback_score = st.slider("Feedback Score", 0, 5, 4)
tenure = st.slider("Tenure", 1, 10, 5)

# Create a DataFrame with user input
user_input = pd.DataFrame({
    'Age': [age],
    'Job': [job],
    'MaritalStatus': [marital_status],
    'Education': [education],
    'AnnualIncome': [annual_income],
    'TransactionHistory': [transaction_history],
    'PaymentPatterns': [payment_patterns],
    'ServiceUsageFrequency': [service_usage_frequency],
    'ServiceUsageDuration': [service_usage_duration],
    'MostUsedFeatures': [most_used_features],
    'SupportInteractions': [support_interactions],
    'FeedbackScore': [feedback_score],
    'Tenure': [tenure]
})

# Make predictions based on user input
if st.button("Predict Churn"):
    # Preprocess user input
    label_encoder = LabelEncoder()
    categorical_cols = user_input.select_dtypes(include=['object']).columns
    user_input[categorical_cols] = user_input[categorical_cols].apply(label_encoder.fit_transform)

    # Standardize numerical features
    scaler = StandardScaler()
    user_input = scaler.fit_transform(user_input)

    # Make predictions
    prediction = model.predict(user_input)

    # Display the result
    st.subheader("Prediction:")
    if prediction[0] == 1:
        st.warning("Churn: Yes")
    else:
        st.success("Churn: No")
