"""
A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a pangram or not.
"""

LETTERS_IN_ALPHABET = 26


def check_is_panagram(sentence):
    letters_for_check = []
    for element in sentence.replace(' ', '').lower():
        if element not in letters_for_check:
            letters_for_check.append(element)
    if len(letters_for_check) == LETTERS_IN_ALPHABET:
        return True
    else:
        return False


print(check_is_panagram('Pack my box with five dozen liquor jugs'))
