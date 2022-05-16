import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


n = inp()
count = 0
num = 0
for i in range(n):
    start, end = inlt()
    for i in range(start, end + 1, 2):
        if i & (i+1) == 0:
            count += 1
    print(count)
