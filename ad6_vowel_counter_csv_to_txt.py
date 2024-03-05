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