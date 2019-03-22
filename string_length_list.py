"""
Write a program that maps a list of words into a list of integers representing the lengths of
the corresponding words. Write it using list comprehensions.
"""


words_list = ['correspond', 'a', 'into', 'words', 'of', 'list', 'a', 'maps', 'that', 'program']


def map_to_lengths_lists(words):
    return [len(word) for word in words]


print(map_to_lengths_lists(words_list))
