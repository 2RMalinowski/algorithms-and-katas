"""
Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing
brackets (in that order), none of which mis-nest.

Examples:
[]        OK   ][        NOT OK
[][]      OK   ][][      NOT OK
[[][]]    OK   []][[]    NOT OK

hint: count a number of opening brackets ("level"), it should not go below 0
"""


def balanced(brackets):
    brackets_level = 0
    control = True
    for bracket in brackets:
        if bracket == '[':
            brackets_level += 1
        else:
            brackets_level -= 1
            if brackets_level < 0:
                control = False
    return brackets_level == 0 and control
    # return not control or brackets_level != 0


print(balanced('[]'))
print(balanced('[][]'))
print(balanced('[[][]]'))

print(balanced(']['))
print(balanced('][]['))
print(balanced('[]][[]'))
