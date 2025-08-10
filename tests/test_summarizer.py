from analyzer.summarizer import summarize_text

def test_summarizer():
    text = "Artificial Intelligence is a rapidly evolving field that aims to create machines capable of human-like intelligence."
    summary = summarize_text(text)
    assert isinstance(summary, str)
    assert len(summary) > 0
