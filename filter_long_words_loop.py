"""
Write a function filter_long_words() that gets a list of words and an integer n
and returns the list of words that are longer than n.
"""


def words_from(words_file ):
    words_list = []
    plain_words_list = []
    with open(words_file, 'r') as sourcefile:
        lines = sourcefile.readlines()
        for line in lines:
            line = line.strip().lower()
            words = line.split()
            words_list.extend(words)
        for word in words_list:
            word = word.replace('.', '')
            word = word.replace(',', '')
            plain_words_list.append(word)
    return plain_words_list


def display_elements(some_list):
    for number, element in enumerate(some_list, 1):
        print(number, element)


def filter_long_words(list_of_words, length_of_word):
    list_of_longer_words = []
    for word in list_of_words:
        if len(word) > length_of_word:
            list_of_longer_words.append(word)
    return list_of_longer_words


display_elements(filter_long_words(words_from('hipster_data.txt'), 12))
