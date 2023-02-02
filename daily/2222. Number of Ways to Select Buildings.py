'''
0 -> 0
1 -> 1

01 -> 01

10 -> 10


'''


class Solution:
    
    
    
    def numberOfWays(self, s: str) -> int:
        
        counter = Counter()
        
        totalWays = 0
        
        for i in range(len(s)):
            building = s[i]
            if building == '1':
                totalWays += counter['10']
                counter['1'] += 1
                counter['01'] += counter['0']
            else:
                totalWays += counter['01']
                counter['0'] += 1
                counter['10'] += counter['1']
        
        return totalWays
            
            
            
            
        
        
        
