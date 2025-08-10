from analyzer.keywords import extract_keywords

def test_keywords():
    text = "AI will change the world and AI is powerful"
    keywords = extract_keywords(text)
    assert "ai" in keywords
