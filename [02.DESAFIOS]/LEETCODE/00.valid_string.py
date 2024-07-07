# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
import re


def isValid(s):
    abre = {'[':']', '(':')', '{':'}'}
    for letra in s:
        if letra in abre.keys():
            if abre[letra] not in s:
                return False
    return True



s = '(]'
print(isValid(s))