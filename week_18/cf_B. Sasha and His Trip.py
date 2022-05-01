
import sys
input = sys.stdin.readline


def inlt():
    return(list(map(int, input().split())))


n, capacity = inlt()
totalFuelNeeded = n - 1
fuel = 0
price = 0
for i in range(1, n):
    while fuel < capacity and fuel < totalFuelNeeded:
        price += i
        fuel += 1
    fuel -= 1
    totalFuelNeeded -= 1
print(price)
