import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import json

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DB_URL = os.getenv("DB_URL")

llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")

print("-- Sentiment Analyzer --")

# Make the sentence an input from the user
sentence = input("Enter the sentence to analyze: ").strip()

prompt_decision = f"""
You are a sentiment analyzer. Analyze the following sentence and determine if it is Positive, Negative, or Neutral.
Provide **only the final sentiment label** without explaining reasoning.

Sentence: "{sentence}"
"""

prompt_reasoning = f"""
You are a sentiment analyzer. Analyze the following sentence and determine if it is Positive, Negative, or Neutral.
Explain your reasoning step by step before giving the final sentiment.

Sentence: "{sentence}"
"""

# Add a flag for user input to choose reasoning or decision-based analysis
flag = input("Do you want reasoning-based analysis? (y/n): ").strip().lower()

if flag == 'y':
    prompt = prompt_reasoning
elif flag == 'n':
    prompt = prompt_decision
else:
    print("Invalid input. Defaulting to decision-based analysis.")
    prompt = prompt_decision

try:
    response = llm.invoke(prompt)
    response_content = response.content.strip()
    print(f"Response : {response_content}")

    # Prepare the JSON output
    output_data = {
        "sentence": sentence,
        "sentiment": "Positive" if "Positive" in response_content else "Negative" if "Negative" in response_content else "Neutral",
        "reasoning": response_content if flag == 'y' else "Reasoning not provided."
    }

    # Write the output to a JSON file
    output_file = "output.json"

    # Check if the file exists and load existing data
    if os.path.exists(output_file):
        with open(output_file, "r") as json_file:
            try:
                existing_data = json.load(json_file)
                # Ensure existing_data is a list
                if isinstance(existing_data, dict):
                    existing_data = [existing_data]
                elif not isinstance(existing_data, list):
                    existing_data = []
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # Append the new data
    existing_data.append(output_data)

    # Write the updated data back to the file
    with open(output_file, "w") as json_file:
        json.dump(existing_data, json_file, indent=4)

    print(f"Output appended to {output_file}")

except Exception as e:
    print(f"Error: {e}")