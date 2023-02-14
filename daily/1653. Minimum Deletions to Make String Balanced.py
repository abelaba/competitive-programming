class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        result = 0
        
        for i in range(len(s)):
            
            if stack and s[i] == "a" and stack[-1] == "b":
                
                stack.pop()
                result += 1
            
            else:
                stack.append(s[i])
        
        return result
