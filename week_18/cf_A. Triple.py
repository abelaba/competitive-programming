import collections
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


t = inp()
answers = []
for i in range(t):
    n = inp()
    array = inlt()
    array.sort()
    answer = -1
    count = 1
    for i in range(len(array) - 1):
        if array[i] != array[i+1]:
            count = 1
        if array[i] == array[i+1]:
            count += 1
        if count >= 3:
            answer = array[i]
    answers.append(answer)

for a in answers:
    print(a)
