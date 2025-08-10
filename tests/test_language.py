from analyzer.language_detect import detect_language

def test_language():
    text = "Halo, apa kabar?"
    lang = detect_language(text)
    assert lang == "id"
