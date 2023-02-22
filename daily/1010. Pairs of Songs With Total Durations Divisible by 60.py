class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        
        count =  0
        pairs = defaultdict(int)
              
            
        for t in time:
            remainder = t%60
            
            count += pairs[(60-remainder) % 60]
            
            pairs[remainder] += 1
        
        return count
