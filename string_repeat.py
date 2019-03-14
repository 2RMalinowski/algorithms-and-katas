"""
Write a method which repeat words in string 'index' times. Do it in 'pythonic way'.
Example:
repeat_string('a wise old owl !')
' wise oldold owlowlowl !!!!'
"""


def repeat_string(text):
    words_form_text_list = text.split()
    return ' '.join([word * words_form_text_list.index(word) for word in words_form_text_list])


print(repeat_string('a wise old owl !'))
print(repeat_string('eeny meeny miny moe !'))
