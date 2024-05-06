# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true


# INACABADO
import re
n = int(input())

for i in range(n):
  s = input()
  s = re.sub("([&]{2})", "and", s)
  s = re.sub("(\| \|)", "or", s) 
print(s)