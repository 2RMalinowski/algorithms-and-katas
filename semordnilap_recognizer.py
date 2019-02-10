"""
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backward.
("Semordnilap" is itself "palindromes" spelled backward.)
Write a semordnilap recognizer that accepts a file name (pointing to a list of words) from the user
and finds and prints all pairs of words that are semordnilaps to the screen.
For example, if "stressed" and "desserts" is part of the word list, the output should include
the pair "stressed desserts". Note: By the way, each pair by itself forms a palindrome! ;)
"""


def words_from(words_file):
    words_list = []
    with open(words_file, 'r') as sourcefile:
        lines = sourcefile.readlines()
        for line in lines:
            words = line.split()
            # line = ["hello", "world", "abc"]
            words_list.extend(words)
    return words_list


print(words_from('semordnilap_data.txt'))


def semordnilap_recognizer(occur_semonilap_list):
    pairs_list = []
    for i in range(len(occur_semonilap_list)):
        for word in occur_semonilap_list:
            if occur_semonilap_list[i] == word[::-1]:
                pairs_list.append(word)

    for semordnilap in pairs_list:
        if semordnilap[::-1] in pairs_list:
            pairs_list.remove(semordnilap)
    return pairs_list


def display_semordnilap_form(semordnilap_list):
    for semordnilap in semordnilap_list:
        print(semordnilap, semordnilap[::-1])


display_semordnilap_form(semordnilap_recognizer(words_from('semordnilap_data.txt')))
