class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        
        count = 0
        
        for i in range(len(nums)):
            temp = nums[i]
            
            for j in range(len(nums)):
                val = nums[j]
                if len(temp) + len(val) == len(target) and i != j:
                    concat = temp+val
                    count += int(concat == target)
                    
        
        return count
                
