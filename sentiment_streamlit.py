import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

# Streamlit app setup
st.title("Sentiment Analyzer")

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DB_URL = os.getenv("DB_URL")

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")

# User input for the sentence
sentence = st.text_input("Enter the sentence to analyze:")

# User input for reasoning-based or decision-based analysis
flag = st.radio("Do you want reasoning-based analysis?", ("Yes", "No"))

# Set the prompt based on user choice
if flag == 'Yes':
    prompt = f"""
    You are a sentiment analyzer. Analyze the following sentence and determine if it is Positive, Negative, or Neutral.
    Explain your reasoning step by step before giving the final sentiment.

    Sentence: "{sentence}"
    """
else:
    prompt = f"""
    You are a sentiment analyzer. Analyze the following sentence and determine if it is Positive, Negative, or Neutral.
    Provide **only the final sentiment label** without explaining reasoning.

    Sentence: "{sentence}"
    """

# Display the prompt
# st.write("### Prompt:")
# st.write(prompt)

# Generate and display the response
if st.button("Analyze Sentiment"):
    try:
        response = llm.invoke(prompt)
        st.success(f"Response: {response.content.strip()}")
    except Exception as e:
        st.error(f"Error: {e}")