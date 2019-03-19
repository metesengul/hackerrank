#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    current_cloud = 0
    while True:
        if current_cloud == len(c) - 1:
            break
        if current_cloud + 2 == len(c):
            jumps += 1
            break

        if c[current_cloud + 2] == 0:
            current_cloud += 2
        else:
            current_cloud += 1
        jumps += 1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
