class Solution:
    def reverseParentheses(self, s: str) -> str:
        firstStack = []
        queue = []
        for i in s:
            if i == ")":
                while True:
                    temp = firstStack.pop()
                    if(temp == "("):
                        break
                    queue.append(temp)
                while len(queue) != 0:
                    temp = queue.pop(0)
                    firstStack.append(temp)
            else:
                firstStack.append(i)
        return ''.join(firstStack)
