import csv
#
vowels = ['a', 'e', 'i', 'o', 'y', 'u', 'A', 'E', 'I', 'O', 'U', 'Y']
#
# csvfile = 'inputs.csv'
# txtfile = 'result.txt'
# def read_file(csvfile):
#     with open(csvfile, mode='w') as file:
#         content = file.read()
#         vowel_counter_d = {i:content.count(i) for i in content if i in vowels}
#         results = txtfile.write(content, vowel_counter_d)
#         return results
#
# read_file(csvfile)

#
# def vowel_counter_dict(given_word):
#     vowel_counter_d = {i:given_word.count(i) for i in given_word if i in vowels}
#     return given_word, vowel_counter_d
#
#
# def save_file(input_word, dict_vowel_counter):
#     input_word = read_file()
#     dict_vowel_counter = vowel_counter_dict(input_word)

#
# import csv
#
# def count_vowels(given_word):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     vowel_counter_d = {i:given_word.count(i) for i in given_word if i in vowels}
#     return vowel_counter_d
# #
# def process_csv_file(input_file, output_file):
#     with open(input_file, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         #data = {row[0]: count_vowels(row[0]) for row in reader}
#         #data = {i:reader.count(i) for i in reader if i in vowels}
#         output = count_vowels(reader)
# #
#     with open(output_file, 'w') as txtfile:
#     # for key, value in count_vowels.items():
#         txtfile.write(f"{reader}{output}")
# #
# # # Process the CSV file 'inputs.csv' and write the results to 'results.txt'
# process_csv_file('inputs.csv', 'results.txt')
# print(count_vowels("bananayoui"))


import csv

def count_vowels(given_word):
    vowels = ['a', 'e', 'i', 'o', 'y', 'u', 'A', 'E', 'I', 'O', 'U', 'Y']
    vowel_counter_d = {i:given_word.count(i) for i in given_word if i in vowels}
    return vowel_counter_d

def process_csv_file(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = {row[0]: count_vowels(row[0]) for row in reader if row}

    with open(output_file, 'w') as txtfile:
        for key, value in data.items():
            txtfile.write(f"{{'{key}' : {value}}}\n")

# Process the CSV file 'inputs.csv' and write the results to 'results.txt'
process_csv_file('inputs.csv', 'results.txt')