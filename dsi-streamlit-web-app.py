
# Import Libraries
import streamlit as st
import pandas as pd
import joblib

# load our model pipeline object
model = joblib.load('model.joblib')

# Add title and instructions
st.title("Purchase Prediction Model")
st.subheader("Enter Customer Information and submit for likelihood to purchase")

# Age input form
age = st.number_input(
    label="01. Enter the customer's age",
    min_value=18,
    max_value=120,
    value=35
)

# Gender input form
gender = st.radio(
    label="02. Enter the customer's gender",
    options=['M', 'F']
)

# Credit Score input form
credit_score = st.number_input(
    label="03. Enter the customer's credit score",
    min_value=0,
    max_value=1000,
    value=500
)


# Submit inputs to model
if st.button(label='Submit For Prediction'):

    # Store our data in a dataframe for prediction
    new_data = pd.DataFrame({'age': [age], 'gender': [gender], 'credit_score': [credit_score]})

    # Apply model pipeline to the input data and extract probability prediction
    pred_proba = model.predict_proba(new_data)[0][1]

    # output prediction
    st.subheader(f'Based on the customer attributes, our model predicts a purchase probabillity of {pred_proba:.0%}.')

    


