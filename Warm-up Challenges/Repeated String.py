#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    divisor = int(n / len(s))
    remainder = n % len(s)
    total = divisor * s.count("a")
    for i in range(remainder):
        if s[i] == "a":
            total += 1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
