class Solution:
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        '''
         000111
         001011
         001101
         010011
         010101 
        '''
        
        openingCount = n
        closingCount = n
        
        answer = []
        
        def helper(stack, openingCount, closingCount):
            
            if openingCount == closingCount == 0:
                answer.append(''.join(stack))
                return
            if openingCount != 0:
                stack.append("(")
                helper(stack, openingCount - 1, closingCount)
                stack.pop()
            if closingCount > openingCount:
                stack.append(")")
                helper(stack, openingCount, closingCount - 1)
                stack.pop()
            
        
        helper([], openingCount, closingCount)
        return answer
            
            
            
