"""
Write a program that given string will create simple permutation of all characters.
For example, permute_characters_form('macao') should gives the following:
['macao', 'acaom', 'caoma', 'aomac', 'omaca']
"""


def permute_characters_form(any_string):
    char_list = []
    for n in range(len(any_string)):
        for char in any_string:
            char_list.append(any_string[n % len(any_string)])
            n += 1
    word_list = [''.join(char_list[char:char + len(any_string)]) for char in range(0, len(char_list), len(any_string))]
    return word_list


print(permute_characters_form('macao'))
