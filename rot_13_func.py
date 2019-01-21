"""
Caesar cipher (with using ord() and chr(), instead defined dictionary)
"""


def rot_as_many_as_wish(sentence, rotation):
    number = 0
    letter_list = []
    for letter in sentence:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            # number in alphabet: a = 0, b = 1, ...
            letter_number = ord(letter) - ord('a')
            rotated_letter_number = (letter_number + rotation) % 26
            rotated_letter = chr(rotated_letter_number + ord('a'))
        elif ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
            letter_number = ord(letter) - ord('A')
            rotated_letter_number = (letter_number + rotation) % 26
            rotated_letter = chr(rotated_letter_number + ord('A'))
        else:
            rotated_letter = letter
        letter_list.append(rotated_letter)
    return ''.join(letter_list)


print(rot_as_many_as_wish('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!', 13))
print(rot_as_many_as_wish('ZnpnqnzvN', 13))
