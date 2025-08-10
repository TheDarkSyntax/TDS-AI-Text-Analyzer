import re
from collections import Counter

def extract_keywords(text, top_n=5):
    words = re.findall(r'\b\w+\b', text.lower())
    common = Counter(words).most_common(top_n)
    return [word for word, _ in common]
