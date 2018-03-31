#!/bin/python3

import os
import sys

def birthdayCakeCandles(n, ar):
    highest = candle_count = 0
    for i in range(n):
        if ar[i] > highest:
            highest = ar[i]
            candle_count = 1
        elif ar[i] == highest:
            candle_count += 1
    return candle_count

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()

