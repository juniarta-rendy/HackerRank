#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    char = [x for x in s]
    shifted_char = []
    for i in char:
        if i.isalpha():
            if i.isupper():
                start = ord('A')
            else:
                start = ord('a')
            result = chr(((ord(i) - start + k) % 26) + start)
            shifted_char.append(result)
        else:
            shifted_char.append(i)
    value = ''.join(shifted_char)
    return value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
