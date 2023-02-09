class Solution:
    
    def restore(self, s, answer, stack, index):
        
        if len(stack) > 4:
            return
        
        if index == len(s):
            if len(stack) == 4:
                answer.append('.'.join(stack))
            return
        
        stack.append(s[index])
        self.restore(s, answer, stack, index+1)
        stack.pop()
        
        if s[index] != "0" and index <= len(s)-2:
            stack.append(s[index: index+2])
            self.restore(s, answer, stack, index+2)
            stack.pop()
        
        if s[index] != "0" and index <= len(s)-3 and int(s[index: index+3]) <= 255:
            stack.append(s[index: index+3])
            self.restore(s, answer, stack, index+3)
            stack.pop()
            
        
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        
        self.restore(s, answer, [], 0)
        
        return answer
