"""
Write a program that given a text file will create a new text file in which all
the lines from the original file are numbered from 1 to n
(where n is the number of lines in the file).
"""


def numerate_lines(source_file, dest_file):
    line_number = 1
    numered_lines = []
    with open(source_file, 'r') as sourcefile:
        lines = sourcefile.readlines()
        for line in lines:
            line = str(line_number) + '. ' + line
            numered_lines.append(line)
            line_number += 1
    with open(dest_file, 'a') as destfile:
        destfile.write(''.join(numered_lines))


# numerate_lines('hipster_data.txt', 'numered_hipster_data.txt')


def numerate_lines_from(source_file, dest_file):
    numered_lines = []
    with open(source_file, 'r') as sourcefile:
        lines = sourcefile.readlines()
        for number, line in enumerate(lines, 1):  # start numerate from 1
            line = f'{number}. {line}'
            numered_lines.append(line)  # append strings to empty list
    with open(dest_file, 'a') as destfile:
        destfile.write(''.join(numered_lines))


numerate_lines_from('hipster_data.txt', 'numered_hipster_data.txt')
