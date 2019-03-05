"""
Write a function char_freq() that takes a string and builds a frequency
listing of the characters contained in it.
Represent the frequency listing as a Python dictionary
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
"""


def display_elements(some_list):
    for element in some_list:
        print(element)


def display_elements_form(some_dict):
    for k, v in some_dict.items():
        print(f'{k} ---> {v}')


def char_freq(some_string):
    occurrence = {}
    for letter in some_string:
        if letter in occurrence:
            occurrence[letter] += 1
        else:
            occurrence[letter] = 1
    return occurrence


# display_elements_form(char_freq('abbabcbdbabdbdbabababcbcbab'))


"""
1. Display a histogram
histogram('aabbbccccd')
- read about Python dictionaries

a **
b ***
c ****
d *
"""


def histogram_from(dictionary):
    histograms_list = []
    for key, value in dictionary.items():
        histograms_list.append(f"{key} {value * '*'}")
    return histograms_list


# display_elements(histogram_from(char_freq('abbabcbdbabdbdbabababcbcbab')))


"""
2. Display a sorted histogram
- read about sorting in Python

d *
a **
b ***
c ****
"""


def sorted_histogram_from(dictionary):
    tuples_list = []
    for key, value in dictionary.items():
        tuples_list.append((key, value))

    sorted_tuples_list = sorted(tuples_list, key=lambda element: element[1])
    histograms_list = []
    for key, value in tuples_list:
        histograms_list.append(f"{key} {value * '*'}")
    return histograms_list


# print(sorted_histogram_from((char_freq('abbabcbdbabdbdbabababcbcbab'))))
display_elements(sorted_histogram_from(
    char_freq('abbabcbdbabdbdbabababcbcbab')))


# or using funcion: sorted(histograms_list, key=len, reverse=True)
