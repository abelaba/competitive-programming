import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


n = inp()
answer = []
for i in range(n):
    s = input()
    sum1 = sum([int(x) for x in s[:3]])
    sum2 = sum([int(x) for x in s[3:6]])
    if sum1 == sum2:
        answer.append("YES")
    else:
        answer.append("NO")


for ans in answer:
    print(ans)
