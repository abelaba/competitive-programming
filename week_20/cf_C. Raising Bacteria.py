import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


n = inp()
binary = bin(n)
count = 0
while n > 0:
    binary = bin(n)
    powerOf2 = 2 ** (len(binary) - 3)
    n -= powerOf2
    count += 1

print(count)
