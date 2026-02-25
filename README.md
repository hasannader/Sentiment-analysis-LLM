Here is a professional and well-structured **README.md** you can directly use in your GitHub repo.

---

# LLM Sentiment Analyzer (Gemini 2.5 Flash)

A sentiment analysis application powered by **Google Gemini 2.5 Flash** that classifies user text as **Positive, Negative, or Neutral**.
The project provides two interfaces:

* **Terminal-based Python script**
* **Streamlit web application**

Users can choose between:

* **Prediction only**
* **Prediction with reasoning**

---

## Features

* Analyze any user-provided sentence
* Powered by **Gemini 2.5 Flash API**
* Two output modes:

  * Final sentiment only
  * Sentiment with step-by-step reasoning
* Two usage options:

  * Command-line interface (CLI)
  * Interactive Streamlit web app

---

## Project Structure

```
├── sentiment_cli.py          # Terminal version
├── sentiment_streamlit.py    # Streamlit app
├── requirements.txt          # Dependencies
├── .env                      # Environment variables (not uploaded to GitHub)
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

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

This key is used to authenticate requests to the Gemini API.

**Important:**

* Do **not** upload `.env` to GitHub
* Add it to `.gitignore`

Example `.gitignore`:

```
.env
__pycache__/
```

---

## Usage

### 1) Terminal Version

Run:

```bash
python sentiment_cli.py
```

You will be prompted to:

* Enter a sentence
* Choose:

  * `y` → with reasoning
  * `n` → sentiment only

Example:

```
Enter the sentence to analyze: I love this product!
Do you want reasoning-based analysis? (y/n): n
Response: Positive
```

---

### 2) Streamlit Web App

Run:

```bash
streamlit run sentiment_streamlit.py
```

Then open the provided local URL in your browser.

Features:

* Text input for sentence
* Radio button to select reasoning mode
* Button to generate sentiment

---

## How It Works

The application:

1. Takes user input
2. Builds a structured prompt
3. Sends the prompt to **Gemini 2.5 Flash**
4. Returns either:

   * Sentiment label only
   * Sentiment + explanation (based on user choice)

---

## Use Cases

* Customer feedback analysis
* Social media sentiment monitoring
* LLM prompt engineering practice
* Learning LangChain + Gemini integration

---

## Notes

* Uses `ChatGoogleGenerativeAI` from LangChain
* Requires an active Gemini API key
* Streamlit version provides a simple UI for quick testing

---

## License

MIT License (optional — update if needed)

---

If you want, I can also give you:

* a **short GitHub description (150–200 chars)**
* a **professional portfolio version** (to impress recruiters)
* a **better folder structure** (with `.gitignore`, Docker, etc.) for a more production-ready repo.
