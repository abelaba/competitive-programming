class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if len(num) == k:
            return "0"

        stack = []

        for i in num:
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        # If k > 0 remove elements
        for i in range(k):
            stack.pop()

        # Remove leading zeros
        for index in range(len(stack)):
            if eval(stack[index]) > 0:
                break

        return ''.join(stack[index:])
