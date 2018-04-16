#!/bin/python3

import os
import sys

def breakingRecords(score):
    min_score = score[0]
    max_score = score[0]
    min_time = 0
    max_time = 0
    for s in score:
        if s > max_score:
            max_score = s
            max_time += 1
        elif s < min_score:
            min_score = s
            min_time += 1
    return [ max_time, min_time ]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)
    print("{} {}".format( result[0], result[1] ) )

    f.write(' '.join(map(str, result)))
    f.write('\n')
    f.close()

