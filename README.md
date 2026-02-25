# LLM Sentiment Analyzer (Gemini 2.5 Flash)

A sentiment analysis application powered by **Google Gemini 2.5 Flash** that classifies user text as **Positive, Negative, or Neutral**.

The project provides two interfaces:

* 🖥 **Terminal-based Python script (CLI)**
* 🌐 **Streamlit web application**

Users can choose between:

* ✅ Prediction only
* 🧠 Prediction with step-by-step reasoning

The CLI version also automatically generates a **JSON output file** containing the analysis result.

---

## Features

* Analyze any user-provided sentence
* Powered by **Gemini 2.5 Flash API**
* Supports two output modes:

  * Sentiment label only
  * Sentiment with reasoning
* Two usage interfaces:

  * Command-line application
  * Interactive Streamlit web app
* Automatic JSON export (CLI version)

---

## Project Structure

```
├── sentiment_cli.py          # Terminal version (generates JSON output file)
├── sentiment_streamlit.py    # Streamlit web app
├── requirements.txt          # Project dependencies
├── output.json               # Contains sentiment analysis decision by sentiment_cli.py
├── .env                      # Environment variables (not pushed to GitHub)
└── README.md
```

---

## Requirements

* Python 3.9+
* Google Gemini API key

Install dependencies:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
langchain
langchain-google-genai
python-dotenv
streamlit
```

---

## Environment Variables (.env)

Create a `.env` file in the root directory of the project:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

This key is required to authenticate requests to the Gemini API.

### Important

* Do NOT upload `.env` to GitHub
* Add it to `.gitignore`

Example `.gitignore`:

```
.env
__pycache__/
```

---

## Usage

---

### 1️⃣ Terminal Version (CLI)

Run:

```bash
python sentiment_cli.py
```

You will be prompted to:

1. Enter a sentence
2. Choose:

   * `y` → reasoning-based analysis
   * `n` → sentiment decision only

### Output

* The sentiment result is displayed in the terminal.
* A **JSON file is automatically generated** containing:

  * The input sentence
  * The final sentiment prediction
  * The reasoning (if selected)

#### Example JSON Output

```json
{
  "sentence": "I love this product!",
  "sentiment": "Positive",
  "reasoning": "The sentence expresses strong positive emotion using the word 'love'."
}
```

If reasoning mode is disabled, the `reasoning` field may be empty or omitted depending on implementation.

---

### 2️⃣ Streamlit Web Application

Run:

```bash
streamlit run sentiment_streamlit.py
```

Then open the local URL provided in your browser.

Features:

* Text input field
* Radio button to select reasoning mode
* Analyze button to generate sentiment
* Displays result directly in the UI

---

## How It Works

1. The user provides a sentence.
2. The system builds a structured prompt based on the selected mode.
3. The prompt is sent to **Gemini 2.5 Flash** via LangChain.
4. The model returns:

   * Sentiment label only
   * Or sentiment + reasoning
5. (CLI version) The result is saved to a JSON file for logging or further processing.

---

## Tech Stack

* Python
* LangChain
* Google Gemini 2.5 Flash
* Streamlit
* python-dotenv

---

## Use Cases

* Customer feedback analysis
* Social media monitoring
* NLP experimentation
* Learning LLM integration with APIs
* Prompt engineering practice

---

## Notes

* Requires a valid Gemini API key.
* Make sure your environment variables are properly configured before running.
* Designed for educational and experimental purposes.

---

## License

MIT License (or update according to your preference)
