"""
Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I".
"""


def reverse(sentence):
    letters_list = []
    for n in range(len(sentence)):
        # n = 0, 1, 2, 3...
        # -n = -1, -2, -3...
        letters_list.append(sentence[-n-1])
    return ''.join(letters_list)


print(reverse("I am testing"))
