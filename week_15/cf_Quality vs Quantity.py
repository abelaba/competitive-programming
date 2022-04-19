# Sum red > Sum Blue
# Count red < Count Blue

import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def qualityVsQuantity(nums):
    nums.sort()

    sumRed = 0
    sumBlue = 0
    countRed = 0
    countBlue = 0

    left = 0
    right = len(nums) - 1

    while left <= right:
        if sumRed <= sumBlue:
            sumRed += nums[right]
            countRed += 1
            right -= 1
        else:
            sumBlue += nums[left]
            countBlue += 1
            left += 1

        if sumRed > sumBlue and countRed < countBlue:
            return "YES"

    return "NO"


t = inp()
answer = []

for _ in range(t):
    n = inp()
    nums = inlt()
    answer.append(qualityVsQuantity(nums))


for ans in answer:
    print(ans)
