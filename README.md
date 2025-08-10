# 📄 TDS-AI-Text-Analyzer

**AI-powered text analysis tool by TheDarkSyntax**
Performs sentiment detection, keyword extraction, language identification, and text summarization using open-source NLP models. Built with Python and Hugging Face Transformers.

---

## 📌 Features

- **Sentiment Analysis** → Detect whether text is **Positive**, **Negative**, or **Neutral**.
- **Keyword Extraction** → Identify the most important words/phrases in a document.
- **Language Detection** → Automatically detect the language of the text.
- **Text Summarization** → Condense long articles into concise summaries.
- **Open Source & Customizable** → You can fine-tune or expand the capabilities for your own needs.

---

## 🚀 Tech Stack

- **Python 3.9+**
- **Hugging Face Transformers** → Pre-trained NLP models
- **NLTK / spaCy** → Tokenization & linguistic processing
- **Scikit-learn** → Machine learning utilities
- **FastAPI (Optional)** → Turn into a web API
- **Pytest** → Unit testing

---

## 📂 Project Structure

```
TDS-AI-Text-Analyzer/
│
├── README.md               # Project documentation
├── requirements.txt        # Dependencies
├── app.py                   # Entry point for running the tool
├── analyzer/               # Core analysis modules
│   ├── __init__.py
│   ├── sentiment.py        # Sentiment analysis logic
│   ├── keywords.py         # Keyword extraction
│   ├── language_detect.py  # Language detection
│   └── summarizer.py       # Text summarization
└── tests/                  # Unit tests
    ├── test_sentiment.py
    ├── test_keywords.py
    ├── test_language.py
    └── test_summarizer.py
```

---

## 🛠 Installation

1. **Clone this repository**

```bash
git clone https://github.com/YourUsername/TDS-AI-Text-Analyzer.git
cd TDS-AI-Text-Analyzer
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 📖 Usage

### 1. Run sentiment analysis

```python
from analyzer.sentiment import analyze_sentiment

text = "I love using AI for my projects!"
result = analyze_sentiment(text)
print(result)  # Output: Positive
```

### 2. Extract keywords

```python
from analyzer.keywords import extract_keywords

text = "Artificial Intelligence is transforming industries across the globe."
keywords = extract_keywords(text)
print(keywords)
```

### 3. Detect language

```python
from analyzer.language_detect import detect_language

text = "Bonjour tout le monde"
lang = detect_language(text)
print(lang)  # Output: French
```

### 4. Summarize text

```python
from analyzer.summarizer import summarize_text

long_text = "..."  # Your long paragraph/article
summary = summarize_text(long_text)
print(summary)
```

---

## 🔍 Example Output

**Input:**

```
The movie was absolutely wonderful! The acting was superb and the visuals were stunning.
```

**Output:**

```
Sentiment: Positive
Keywords: ['movie', 'acting', 'visuals']
Language: English
Summary: "The movie was wonderful with superb acting and stunning visuals."
```

---

## 📅 Roadmap

- [ ] Add web interface with **Streamlit**
- [ ] Deploy as **FastAPI** service
- [ ] Add named entity recognition (NER)
- [ ] Support more languages for summarization
- [ ] Implement real-time text analysis API

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Commit your changes
4. Push to your fork & submit a Pull Request

---

## 📜 License

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

## 🌟 Credits

Built with ❤️ by **TheDarkSyntax** using open-source AI models and NLP libraries.
