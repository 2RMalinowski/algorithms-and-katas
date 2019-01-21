"""
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
"""


def histogram(numbers):
    for number in numbers:
        print('*' * number)


histogram([4, 9, 0, 7])
