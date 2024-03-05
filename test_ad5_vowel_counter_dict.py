from ad5_vowel_counter_dict import *

def test_count_vowels_empty_input():
    assert vowel_counter_dict("") == {}

def test_count_vowels_no_vowels():
    assert vowel_counter_dict("wxz") == {}

def test_count_vowels_all_vowels():
    assert vowel_counter_dict("aeiouy") == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'y': 1, 'u': 1}

def test_count_vowels_mixed_input():
    assert vowel_counter_dict("hello world") == {'e': 1, 'o': 2}

def test_count_vowels_uppercase_input():
    assert vowel_counter_dict("HELLO WORLD") == {'E': 1, 'O': 2}

def test_count_vowels_special_characters():
    assert vowel_counter_dict("!@#$%^&*()") == {}