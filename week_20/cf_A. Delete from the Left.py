import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


word1 = input()
word2 = input()
word1 = word1[::-1]
word2 = word2[::-1]

word1Length = len(word1)
word2Length = len(word2)
maxLength = max(word1Length, word2Length)
index1 = 0
index2 = 0
for i in range(maxLength):
    if i >= word1Length or i >= word2Length:
        if index1 == 0 and index2 == 0:
            index1 = word1Length
            index2 = word2Length
        break

    if word1[i] != word2[i]:
        break
    else:
        index1 = i
        index2 = i
if index1 == word1Length and index2 == word2Length:
    print(word1Length + word2Length)
else:
    print(word1Length + word2Length - index1 - 1 - index2 - 1)
