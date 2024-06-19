import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())
    soma = 0
    for t_itr in range(t):
        n = int(input().strip())
        for i in range(n):
            if i%3 == 0 or i%5 == 0:
                soma += i
        print(soma)
        soma = 0