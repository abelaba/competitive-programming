class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        while(True):
            if(len(pushed) != 0):
                stack.append(pushed[0])
                pushed.pop(0)
            while(stack[-1] == popped[index]):
                stack.pop()
                index += 1
                if(len(popped) == index or len(stack) == 0):
                    break
            if(stack == [] and len(pushed) == 0):
                break
            elif(len(pushed) == 0 and stack[-1] != popped[index]):
                break

        return stack == []
