"""
An hapax legomenon (often abbreviated to) is a word which occurs only once in either the written record
of a language, the works of an author, or in a single text. Define a function that given the file name
of a text will return all its hapaxes. Make sure your program ignores capitalization.
"""


def words_from(words_file):
    words_list = []
    plain_words_list = []
    with open(words_file, 'r') as sourcefile:
        lines = sourcefile.readlines()
        for line in lines:
            line = line.strip().lower()
            # line = "hello world abc"
            words = line.split()
            # line = ["hello", "world", "abc"]
            words_list.extend(words)
        for word in words_list:
            word = word.replace('.', '')
            word = word.replace(',', '')
            plain_words_list.append(word)
    return plain_words_list


# print(words_from('hipster_data.txt'))


def get_unique(words):
    occurrence = {}
    unique_elements = []
    for word in words:
        if word in occurrence:
            occurrence[word] += 1
        else:
            occurrence[word] = 1
    for k, v in occurrence.items():
        if v == 1:
            unique_elements.append(k)
    return unique_elements


print(get_unique(words_from('hipster_data.txt')))
