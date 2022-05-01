import sys
input = sys.stdin.readline


def inlt():
    return(list(map(int, input().split())))


leftJoystick, rightJoystick = inlt()
minutesPlayed = 0
while leftJoystick and rightJoystick:

    if leftJoystick - 2 <= 0 and rightJoystick - 2 <= 0:
        if leftJoystick - 2 >= 0 or rightJoystick - 2 >= 0:
            minutesPlayed += 1
        break

    if leftJoystick < rightJoystick:
        while rightJoystick - 2 > 0:
            leftJoystick += 1
            rightJoystick -= 2
            minutesPlayed += 1
    else:
        while leftJoystick - 2 > 0:
            leftJoystick -= 2
            rightJoystick += 1
            minutesPlayed += 1

print(minutesPlayed)
