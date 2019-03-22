"""
Write a program that maps a list of words into a list of integers representing the lengths of
the corresponding words. Write it using the higher order function map()
"""

words_list = ['correspond', 'a', 'into', 'words', 'of', 'list', 'a', 'maps', 'that', 'program']


def map_to_lengths_lists(words):
    return map(len, words)


print(list(map_to_lengths_lists(words_list)))
