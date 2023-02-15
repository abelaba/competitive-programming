class Solution:
    
    def checkValidity(self, memo, s, index, openCount):
        state = (index, openCount)
        
        if state in memo:
            return memo[state]
        
        if openCount < 0:
            return False
        
        if index == len(s):
            return openCount == 0
        
        if s[index] == "(":
            memo[state] = self.checkValidity(memo, s, index+1, openCount+1)
            return memo[state]
        
        if s[index] == ")":
            memo[state] = self.checkValidity(memo, s, index+1, openCount-1)
            return memo[state]
        
        else:
            check1 = self.checkValidity(memo, s, index+1, openCount)
            check2 = self.checkValidity(memo, s, index+1, openCount+1)
            check3 = self.checkValidity(memo, s, index+1, openCount-1)
            
            memo[state] = check1 or check2 or check3
            return memo[state]
        
        
    
    def checkValidString(self, s: str) -> bool:
        memo = {}
        
        return self.checkValidity(memo, s, 0, 0)
