from transformers import pipeline

summarizer_pipeline = pipeline("summarization")

def summarize_text(text, max_len=50):
    result = summarizer_pipeline(text, max_length=max_len, min_length=10, do_sample=False)
    return result[0]['summary_text']
