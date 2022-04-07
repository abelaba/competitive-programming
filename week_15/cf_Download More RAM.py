import heapq
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def findMaxRam(n, k, a, b):
    heap = []

    for i in range(n):
        heapq.heappush(heap, (a[i], b[i]))

    while heap:
        popped = heapq.heappop(heap)
        if popped[0] <= k:
            k += popped[1]

    return k


ans = []
for i in range(inp()):
    n, k = inlt()
    a = inlt()
    b = inlt()

    ans.append(findMaxRam(n, k, a, b))

for ram in ans:
    print(ram)
