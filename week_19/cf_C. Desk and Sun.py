
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def solution(chairs, light):
    chairsInTheSun = 0
    for i in range(light[0], light[2] + 1):
        if i in chairs:
            for c in chairs[i]:
                if light[1] <= c <= light[3]:
                    chairsInTheSun += 1
    return chairsInTheSun


n, m = inlt()  # Number of chairs, Total time
chairs = {}
for i in range(n):
    x, y = inlt()
    if x not in chairs:
        chairs[x] = [y]
    else:
        chairs[x].append(y)

answer = []
for i in range(m):
    light = inlt()
    answer.append(solution(chairs, light))


for ans in answer:
    print(ans)
