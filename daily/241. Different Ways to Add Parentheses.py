class Solution:
    
    def findWays(self, memo, expression):
        
        if expression in memo:
            return memo[expression]
        
        if expression.isdigit():
            memo[expression] = int(expression)
            
            return [int(expression)]
        
        result = []
        operations = "+-*"
        
        for i, char in enumerate(expression):
            
            if char in operations:
                
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                for l in left:
                    for r in right:
                        if char == "+":
                            result.append(l+r)
                        elif char == "-":
                            result.append(l-r)
                        else:
                            result.append(l*r)
                
        memo[expression] = result
        
        return result
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        return self.findWays(memo, expression)
