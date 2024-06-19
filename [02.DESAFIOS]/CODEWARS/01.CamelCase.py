# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, 
# also often referred to as Pascal case). 
# The next words should be always capitalized.
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

text = "the-stealth-warrior"

def to_camel_case(text):
  capitalizar = False
  newText = ""
  for letra in range(len(text)):
    if text[letra] == '_' or text[letra] == "-":
      capitalizar = True
    else:
      if capitalizar:
        newText += text[letra].upper()
        capitalizar = False
      else:
        newText += text[letra]


  print(newText)

to_camel_case(text)