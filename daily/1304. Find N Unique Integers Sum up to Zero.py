class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        
        if n % 2 != 0:            
            n -= 1
            answer.append(0)
        
        i = 1
        while i < n: 
            answer.append(-i)
            answer.append(i)
            i += 2
        
        return answer
            
