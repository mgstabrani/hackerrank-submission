#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    jam = int(s[:2])
    if(s[8] == 'P'):
        if(jam != 12):
            jam += 12
    else:
        if(jam == 12):
            jam = 0
    if(jam < 9):
        jam = "0" + str(jam)
    else:
        jam = str(jam)
    return jam + s[2:8]
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()