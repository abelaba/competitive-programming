import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


t = inp()
answer = []
for i in range(t):
    s = inp()
    candies = inlt()
    minCandy = min(candies)
    candiesAte = 0
    for candy in candies:
        candiesAte += (candy - minCandy)
    answer.append(candiesAte)


for ans in answer:
    print(ans)
