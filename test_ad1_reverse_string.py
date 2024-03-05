import pytest
from ad1_reverse_string import *


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("12345") == "54321"
    assert reverse_string("") == ""


def test_reverse_string_edge_cases():
    assert reverse_string("a") == "a"
    assert reverse_string("ab") == "ba"
    assert reverse_string("racecar") == "racecar"


