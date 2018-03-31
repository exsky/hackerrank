#!/bin/python3

import os
import sys

def miniMaxSum(arr):
    min = max = sum = None
    for n in arr:
        if not sum:
            min = max = sum = n
            continue
        if max < n:
            max = n
        if min > n:
            min = n
        sum += n
    print(sum-max, sum-min)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

