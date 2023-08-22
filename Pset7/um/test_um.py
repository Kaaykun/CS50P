from um import count
import pytest

def test_ignorecase():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_word_containing_um():
    assert count("Yummy cucumber") == 0


def test_surrounded_by_spaces():
    assert count("Hey um are you waiting?") == 1
    assert count("um?") == 1
