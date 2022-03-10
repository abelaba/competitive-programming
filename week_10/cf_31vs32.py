
def inp():
    return(int(input()))


def howManyItTakes(number, k):
    count = 0
    while number != k:
        if number < k:
            number += 4
        elif number > k:
            number -= 1
        count += 1
    return count


def main(k):
    count_31 = howManyItTakes(31, k)
    count_32 = howManyItTakes(32, k)

    if count_31 > count_32:
        print(32)
    else:
        print(31)


inputs = inp()
test_cases = []
for i in range(inputs):
    test_cases.append(inp())

for k in test_cases:
    main(k)
