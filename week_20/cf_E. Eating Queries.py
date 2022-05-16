import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def find(sums, query):
    left = 0
    right = len(sums) - 1
    answer = -1
    while left <= right:
        middle = left + (right - left) // 2

        if sums[middle] >= query:
            answer = middle + 1
            right = middle - 1
        else:
            left = middle + 1
    return answer


t = inp()
answer = []
for i in range(t):
    n, m = inlt()
    candies = inlt()
    candies.sort(reverse=True)
    sums = []
    su_m = 0
    for i in range(n):
        su_m += candies[i]
        sums.append(su_m)
    for i in range(m):
        query = inp()
        answer.append(find(sums, query))


for ans in answer:
    print(ans)
