import re
S = "abaabaabaabaaei"
padrao = re.compile(r'(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])')
check_string = padrao.findall(S)

for substrings in check_string:
  print(substrings)
if not check_string:
  print(-1)
  