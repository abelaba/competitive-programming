import math
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


t = inp()

for i in range(t):
    n, k = inlt()
    binaryOfK = bin(k)
    su_m = 0
    power = 0
    for bit in binaryOfK[::-1]:
        if bit == '1':
            su_m += n ** power
        power += 1
    print(int(su_m) % (10**9 + 7))
