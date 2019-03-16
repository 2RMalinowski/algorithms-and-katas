"""
Write a version of a palindrome recognizer (previous exercise) that accepts a file name from the user,
reads each line, and prints the line to the screen if it is a palindrome.
"""
import os


def filename_input():
    while True:
        source_file_name = input('Enter name of file to read: ')
        if not os.path.isfile(source_file_name):
            print("There isn't such file")
        else:
            return source_file_name


def phrases_from(phrase_file):
    phrases_list = []
    with open(phrase_file, 'r') as sourcefile:
        lines = sourcefile.readlines()
        for line in lines:
            line = line.strip()
            phrases_list.append(line)
    return phrases_list


def is_palindrome(sentences_list):
    palindrome_list = []
    for sentence in sentences_list:
        check_sentence = sentence.replace(' ', '').lower()
        if check_sentence == check_sentence[::-1]:
            palindrome_list.append(sentence)
    return palindrome_list


for palindrome in is_palindrome(phrases_from(filename_input())):
    print(palindrome)
