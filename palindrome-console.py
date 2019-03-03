"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.
"""


def is_palindrome(sentence):
    check_sentence = sentence.replace(' ', '').lower()
    return check_sentence == check_sentence[::-1]


print(is_palindrome('Never odd or even'))
