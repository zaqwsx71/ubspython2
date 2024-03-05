def reverse_string(input_string):
    string_input = list(input_string)
    length = len(string_input)
    first_index = 0
    last_index = length - 1

    while first_index < length/2:
        temp = string_input[last_index]
        string_input[last_index] = string_input[first_index]
        string_input[first_index] = temp
        first_index += 1
        last_index -= 1

    return ''.join(string_input)