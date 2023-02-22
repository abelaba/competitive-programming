class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        
        s = list(s)
        
        totalCount = 0
        
        count = 1
        
        while count != 0:
            
            count = 0
            i = 0
            
            while i < len(s)-1:
                if s[i] == '0' and s[i+1] == '1':
                    count += 1
                    s[i], s[i+1] = s[i+1], s[i]
                    i+=2
                else:
                    i+= 1
            
            if count != 0:
                totalCount += 1

        
                
        return totalCount
