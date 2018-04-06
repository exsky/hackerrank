#!/bin/python3

import os
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    pts_Larry = 0
    pts_Rob = 0
    
    for i in apples:
        if a + i >= s and a + i <= t:
            pts_Larry += 1
    
    for i in oranges:
        if b + i >= s and b + i <= t:
            pts_Rob += 1
    
    print(pts_Larry)
    print(pts_Rob)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)

