from fuel import convert, gauge
import pytest

def test_valid_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valuerror():
    with pytest.raises(ValueError):
        convert("cat/dog")