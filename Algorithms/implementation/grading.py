#!/bin/python3

import os
import sys

def gradingStudents(grades):
    for i in range(n):
        grade = grades[i]
        rank = int( grade/5 )
        modi = int( (grade+2)/5 )
        if modi < 8 :
            continue
        elif rank+1 == modi :
            grades[i] = modi*5
    return grades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

