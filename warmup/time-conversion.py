#!/bin/python3

import os
import sys

def timeConversion(s):
    meridiem = s[-2:]
    hour = int(s[0:2])
    if meridiem == "PM":
        if hour == 12:
            return str(12)+s[2:8]
        else:
            return str(hour+12)+s[2:8]
    else:
        if hour == 12:
            return "00"+s[2:8]
        else:
            return s[:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

