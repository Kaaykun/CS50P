from plates import is_valid

def test_length():
    assert is_valid("OUTATIME") == False
    assert is_valid("O") == False

def test_letterstart():
    assert is_valid("123456") == False
    assert is_valid("A12345") == False

def test_punctuation():
    for punctuation in [" ", ",", ".", ";", ":", "!", "?"]:
        assert is_valid(f"CS{punctuation}50") == False

def test_digit_placement():
    assert is_valid("CS50A") == False

def test_first_digit():
    assert is_valid("CS050") == False

