#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    updatedGrades = []
    for grade in grades:
        if(grade < 38):
            updatedGrades.append(grade)
            continue
        elif ((grade + 2) % 5 == 0):
            updatedGrades.append(grade + 2)
        elif ((grade + 1) % 5 == 0):
            updatedGrades.append(grade + 1)
        else:
            updatedGrades.append(grade)
    return updatedGrades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
