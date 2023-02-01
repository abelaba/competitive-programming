class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        plantGrowPair = [[plantTime[i], growTime[i]] for i in range(len(growTime))]
        plantGrowPair.sort(key=lambda x: (-x[1]))
        
                
        length = 0
        start = 0
        
        for pTime, gTime in plantGrowPair:
            start += pTime
            length = max(length, start+gTime)
        
        return length
        
