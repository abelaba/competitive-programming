
import sys
import math
input = sys.stdin.readline


def inlt():
    return(list(map(int, input().split())))


inputs = inlt()

days = inputs[0]
number_of_days = [day for day in range(days)]
days_assistants_come = []
for i in range(inputs[1]):
    days_assistants_come.append(inlt())

for assistant_day in days_assistants_come:
    for work_day in number_of_days[::-1]:
        if assistant_day[0] <= work_day <= assistant_day[1]:
            number_of_days.remove(work_day)
        elif assistant_day[1] < number_of_days[0]:
            break
if number_of_days:
    print("NO")
else:
    print("YES")
