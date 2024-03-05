vowels = ['a', 'e', 'i', 'o', 'y', 'u', 'A', 'E', 'I', 'O', 'U', 'Y']

def vowel_counter_dict(given_word):
    vowel_counter_d = {i:given_word.count(i) for i in given_word if i in vowels}
    return vowel_counter_d


