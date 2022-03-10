# Input
# Each test case will begin with 2 integers, n (1≤n≤104) and m (1≤m≤105),
# the number of questions and the number of students respectively.
# The next line will contain a space separated integer array b (0≤bi≤106) of size m,
# representing the difficulties that the students are comfortable solving.
# After that, n lines will follow and the i-th line will contain one integer ai (1≤ai≤106),
# the difficulty of the i-th question.

# Output
# For each of the n lines, print out "YES" (without the quotes) if the question would be a good second question and "NO" otherwise
import sys
import math
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


questions, students = invr()

ability = inlt()
ability.sort()


def goodQuestion(difficulty, ability, students):
    l = 0
    r = students-1
    mid = l + (r-l)//2

    while l <= r:
        mid = l + (r-l)//2

        if ability[mid] <= difficulty:
            l = mid + 1
        elif ability[mid] > difficulty:
            r = mid - 1

    if l < students - r and r > 0:
        print(r)
        print("YES")
    else:

        print("NO")


for i in range(questions):
    difficulty = inp()
    goodQuestion(difficulty, ability, students)
