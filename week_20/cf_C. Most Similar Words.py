import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


t = inp()
answer = []
for i in range(t):
    n, m = inlt()
    words = []
    for i in range(n):
        words.append(input().strip())

    minDifference = sys.maxsize
    for i in range(n):
        firstWord = words[i]
        for j in range(i+1, n):
            nextWord = words[j]
            difference = sum(
                [abs(ord(firstWord[x]) - ord(nextWord[x])) for x in range(m)])
            minDifference = min(minDifference, difference)
    answer.append(minDifference)

for ans in answer:
    print(ans)
