def read_file(file):
    with open(file) as file:
        content = file.read().strip()
        return content

def count_words_from_file(content):
    if len(content) == 0:
        return 0
    return content.count(' ') + 1

x = read_file("file.txt")
result = count_words_from_file(x)

print(result)


