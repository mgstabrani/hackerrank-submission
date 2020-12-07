#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the andProduct function below.
def andProduct(a, b):
    result = a
    for i in range(a+1,b+1):
        result = result & i
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
