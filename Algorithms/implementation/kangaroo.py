#!/bin/python3

import sys

# x1 + v1 * t = x2 + v2 * t
# x1 - x2 = ( v2 - v1 ) * t
# (x1 - x2) / ( v2 - v1 ) = t
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return 'YES';
        else:
            return 'NO';
        
    t = (x1 - x2) / ( v2 - v1 )
    if t < 0:
        return 'NO';
    if t == int(t):
            return 'YES'
    return 'NO'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

