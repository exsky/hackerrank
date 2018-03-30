#!/bin/python3

import os
import sys

def aVeryBigSum(n, ar):
    # The integer size of python
    # Try print( sys.maxsize )
    # The value is 9223372036854775807, 2^63-1 
    sum = 0
    for i in ar:
        sum += i
    return sum

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()
