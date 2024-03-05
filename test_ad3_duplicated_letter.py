from ad3_duplicated_letter import *

def test_has_duplicated_letters():
    assert has_duplicated_letters("hello") == True
    assert has_duplicated_letters("world") == False
    assert has_duplicated_letters("python") == False
    assert has_duplicated_letters("testing") == True