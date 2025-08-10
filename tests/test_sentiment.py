from analyzer.sentiment import analyze_sentiment

def test_sentiment():
    text = "I love AI and TheDarkSyntax!"
    result = analyze_sentiment(text)
    assert "POSITIVE" in result or "NEGATIVE" in result
