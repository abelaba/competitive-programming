class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['[', '{', '(']
        closing = [']', '}', ')']
        stack = []

        if(len(s) % 2 != 0):
            return False

        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if(len(stack) != 0):
                    ele = stack.pop()
                    if opening.index(ele) != closing.index(i):
                        return False
                else:
                    return False
        if(len(stack) > 0):
            return False

        return True
