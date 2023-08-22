from numb3rs import validate

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("666.1.1.1") == False
    assert validate("1.666.1.1") == False
    assert validate("1.1.666.1") == False
    assert validate("1.1.1.666") == False

def test_formatting():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False