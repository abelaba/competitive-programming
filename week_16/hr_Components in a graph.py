#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#


def find(parent, x):

    root = x
    while parent[root] != root:
        root = parent[root]

    return root


def union(parent, x, y):
    parent[find(parent, x)] = find(parent, y)


def componentsInGraph(gb):
    # Write your code here
    length = len(gb)
    parent = {}

    for i, j in gb:
        parent[i] = i
        parent[j] = i

    for i, j in gb:
        union(parent, j, i)
        print(parent)

    answer = collections.defaultdict(lambda: 0)

    ma_x = 0

    for i in parent:
        p = find(parent, i)
        answer[p] += 1
        value = answer[p]

        if value > ma_x:
            ma_x = value

    mi_n = min(answer.values())

    return [mi_n, ma_x]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
