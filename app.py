import streamlit as st
import joblib

#  Step 1: Load your model
model = joblib.load("best_model_LinearSVC.pkl")

#  Step 2: Make a title
st.title(" Twitter Sentiment Analysis App")

#  Step 3: Ask the user to type a message
user_text = st.text_input("Tweet here:")

# Step 4: When they click the button
if st.button("Predict Sentiment"):
    if user_text.strip() == "":
        st.write("Please type something!")
    else:
        # Ask model to predict
        prediction = model.predict([user_text])
        
        # Show result
        st.write("The Sentiment is:", prediction[0])
