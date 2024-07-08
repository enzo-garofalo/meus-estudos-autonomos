# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
import re


def isValid(s):
    pairs = {'[':']', 
             '(':')', 
             '{':'}'}

    expected = []
    for letra in s:
        if letra in pairs.keys():
            expected.append(pairs[letra])
            if pairs[letra] not in s:
                return False
        elif len(expected) == 0:
            return False
        elif letra != expected.pop():
            return False
    if len(expected) > 0:
        return False
    return True

s = '[[[]'
print(isValid(s))