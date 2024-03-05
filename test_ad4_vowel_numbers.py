from ad4_vowel_numbers import *


def test_count_vowels_empty_input():
    assert vowel_counter("") == 0

def test_count_vowels_no_vowels():
    assert vowel_counter("wzx") == 0

def test_count_vowels_all_vowels():
    assert vowel_counter("aeiouy") == 6

def test_count_vowels_mixed_input():
    assert vowel_counter("hello world") == 3

def test_count_vowels_uppercase_input():
    assert vowel_counter("HELLO WORLD") == 3

def test_count_vowels_special_characters():
    assert vowel_counter("!@#$%^&*()") == 0