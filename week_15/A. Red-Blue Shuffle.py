import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


l = inp()
answers = []

for _ in range(l):
    n = inp()
    a = [x for x in input()]
    b = [x for x in input()]

    aIsGreater = bIsGreater = 0

    for i in range(n):
        if a[i] > b[i]:
            aIsGreater += 1
        elif a[i] < b[i]:
            bIsGreater += 1

    if aIsGreater > bIsGreater:
        answers.append("RED")
    elif aIsGreater < bIsGreater:
        answers.append("BLUE")
    else:
        answers.append("EQUAL")

for answer in answers:
    print(answer)
