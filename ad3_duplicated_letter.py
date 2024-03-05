def has_duplicated_letters(string):
    for char in string:
        if string.count(char) > 1:
            return True
    return False

string1 = "zaqwsx"
string2 = "kajak"
result1 = has_duplicated_letters(string1)
result2 = has_duplicated_letters(string2)
print(result1)
print(result2)