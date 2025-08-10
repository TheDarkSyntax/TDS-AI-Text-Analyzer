from analyzer.sentiment import analyze_sentiment
from analyzer.keywords import extract_keywords
from analyzer.language_detect import detect_language
from analyzer.summarizer import summarize_text

if __name__ == "__main__":
    text = input("Masukkan teks untuk dianalisis: ")
    print(f"Bahasa: {detect_language(text)}")
    print(f"Sentimen: {analyze_sentiment(text)}")
    print(f"Keyword: {extract_keywords(text)}")
    print(f"Ringkasan: {summarize_text(text)}")
