import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def solution(n, nthList):
    stack = []
    for i in nthList:
        if stack and stack[-1] < i:
            while stack and stack[-1] < i:
                stack.pop()
        stack.append(i)
    return len(nthList) - len(stack)


answer = []
n = inp()  # Number of columns
for i in range(n):
    n1 = inp()
    n1List = inlt()
    answer.append(solution(n1, n1List))

for ans in answer:
    print(ans)
