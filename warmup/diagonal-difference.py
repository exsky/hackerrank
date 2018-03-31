#!/bin/python3

import os
import sys
import math

# 0 1 2
# 3 4 5
# 6 7 8
def diagonalDifference(a):
    size = len(a)
    diagonal_primary = 0
    diagonal_secondary = 0
    for i in range(size):
        diagonal_primary += a[i][i]
        diagonal_secondary += a[i][size-1-i]
    difference_val = diagonal_primary - diagonal_secondary
    return difference_val if difference_val > 0 else -difference_val

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()

