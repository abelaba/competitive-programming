import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


answer = []
t = inp()
for i in range(t):
    n, m = inlt()  # Number of students, Number of outlets

    a = inlt()  # Outlets created

    a.sort(reverse=True)

    i = 0
    su_m = 2
    while su_m < n and i < len(a):
        su_m += a[i] - 1
        i += 1

    if su_m >= n:
        answer.append(i)
    else:
        answer.append(-1)
for ans in answer:
    print(ans)
