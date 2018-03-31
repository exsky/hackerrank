#!/bin/python3

import os
import sys

def plusMinus(arr):
    positive_num = negative_num = zeros_num = 0
    #negative_num = 0
    #zeros_num = 0
    for num in arr:
        if num > 0: 
            positive_num += 1
        elif num < 0: 
            negative_num += 1
        else: 
            zeros_num += 1
    print( "%.6f" % (positive_num/n) )
    print( "%.6f" % (negative_num/n) )
    print( "%.6f" % (zeros_num/n) )
            
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

