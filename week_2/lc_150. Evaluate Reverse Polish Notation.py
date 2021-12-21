class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i in signs:
                a = eval(stack.pop())
                b = eval(stack.pop())
                if i == "+":
                    stack.append(str(int(b + a)))
                elif i == "-":
                    stack.append(str(int(b - a)))
                elif i == "*":
                    stack.append(str(int(b * a)))
                elif i == "/":
                    stack.append(str(int(b / a)))
            else:
                stack.append(i)
        return stack.pop()
