import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


t = inp()

for i in range(t):
    word = input()
    lastIndex = len(word) - 2
    index = 0
    while word[lastIndex] == 'a':
        index += 1
        lastIndex -= 1

    if index < len(word) - 1:
        word = list(word)
        word.insert(index, "a")

        print("YES")
        print(''.join(word))
    else:
        print("NO")
