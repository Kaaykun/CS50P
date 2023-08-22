from seasons import minutes_old, check_date
from datetime import date
import pytest


def test_output():
    assert check_date("2023-05-09") == date(2023, 5, 9)