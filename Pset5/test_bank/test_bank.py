from bank import value

def test_0():
    assert value("hello, how are you") == 0
    assert value("HELLO, HOW ARE YOU") == 0

def test_20():
    assert value("hey there, welcome") == 20
    assert value("HEY THERE, WELCOME") == 20

def test_100():
    assert value("good evening to you") == 100
    assert value("GOOD EVENING TO YOU") == 100