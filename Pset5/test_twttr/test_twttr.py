from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixedcase():
    assert shorten("TwiTtEr") == "TwTtr"

def test_numbers():
    assert shorten("123456789") == "123456789"

def test_punctuation():
    assert shorten(",.'!?;*") == ",.'!?;*"
