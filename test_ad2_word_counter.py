from ad2_word_counter import *

def test_count_words_from_file():
    content = "This is a test sentence."
    assert count_words_from_file(content) == 5

def test_count_words_from_file_empty():
    content = ""
    assert count_words_from_file(content) == 0