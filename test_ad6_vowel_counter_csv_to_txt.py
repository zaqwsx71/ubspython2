import csv
from ad6_vowel_counter_csv_to_txt import count_vowels, process_csv_file

def test_count_vowels():
    assert count_vowels("hello") == {'e': 1, 'o': 1}
    assert count_vowels("Python") == {'o': 1, 'y': 1}
    assert count_vowels("AEIOU") == {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}

def test_process_csv_file():
    input_file = "test_input.csv"
    output_file = "test_output.txt"

    with open(input_file, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["hello"])
        writer.writerow(["Python"])
        writer.writerow(["AEIOU"])

    with open(output_file, 'r') as txtfile:
        lines = txtfile.readlines()
        assert len(lines) == 3
        assert lines[0] == "{'hello' : {'e': 1, 'o': 1}}\n"
        assert lines[1] == "{'Python' : {'y': 1, 'o': 1}}\n"
        assert lines[2] == "{'AEIOU' : {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}}\n"

    process_csv_file(input_file, output_file)
