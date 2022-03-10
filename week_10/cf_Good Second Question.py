import sys
input = sys.stdin.readline


def inlt():
    return(list(map(int, input().split())))


def inp():
    return(int(input()))


def main():
    inputs = inlt()

    difficulty_willing_to_answer = inlt()

    test_cases = []
    for i in range(inputs[0]):
        test_cases.append(inp())

    difficulty_willing_to_answer.sort(reverse=True)

    mid = len(difficulty_willing_to_answer) // 2

    for k in test_cases:
        if k <= difficulty_willing_to_answer[mid] and k > difficulty_willing_to_answer[-1]:
            print("YES")
        else:
            print("NO")


main()
