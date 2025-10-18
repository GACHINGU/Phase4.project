import streamlit as st
import joblib

# Step 1: Load your trained model
model = joblib.load("best_model_LinearSVC.pkl")

# Step 2: Make a title
st.title("🌟 Twitter Sentiment Analysis App")

# Step 3: Ask user for their tweet
user_text = st.text_input("Type your tweet here:")

# Step 4: When button is clicked
if st.button("Predict Sentiment"):
    if user_text.strip() == "":
        st.warning("⚠️ Please type something first!")
    else:
        # Step 5: Model prediction (returns 0, 1, or 2)
        prediction = model.predict([user_text])[0]

        # Step 6: Match number to meaning
        if prediction == 0:
            sentiment = "😡 Negative"
        elif prediction == 1:
            sentiment = "😊 Positive"
        else:
            sentiment = "😐 Neutral"

        # Step 7: Show result
        st.success(f"The sentiment is: **{sentiment}**")