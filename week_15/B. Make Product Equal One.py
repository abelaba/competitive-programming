
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


n = inp()

nums = inlt()

nums.sort()


negativeNumbers = 0
negativeIndex = 0

for i in range(n):
    if nums[i] > 0:
        break
    else:
        negativeIndex = i
        negativeNumbers += 1

coin = 0

if negativeNumbers % 2 != 0:

    coin = 1 - nums[negativeIndex]
    nums[negativeIndex] = 1

for num in nums:
    if num > 0:
        coin += num - 1
    else:
        coin += abs(num + 1)

print(coin)
