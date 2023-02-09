class Solution:
    def maximumSwap(self, num: int) -> int:
        
        max_ = int(num)
        num = list(str(num))
        
        
        for i in range(len(num)):
            
            for j in range(len(num)):
                
                num[i], num[j] = num[j], num[i]
                max_ = max(max_, int(''.join(num)))
                num[j], num[i] = num[i], num[j]
        
        return max_ 
        
        
            
            
            
            
        
