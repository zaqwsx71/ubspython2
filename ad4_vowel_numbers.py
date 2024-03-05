vowels = ['a', 'e', 'i', 'o', 'y', 'u', 'A', 'E', 'I', 'O', 'U', 'Y']

#given_word = 'banana'

def vowel_counter(given_word):
    vowel_counter = sum(1 for i in given_word if i in vowels)
    return vowel_counter



