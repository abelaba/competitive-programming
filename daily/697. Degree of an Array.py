class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        maxFrequency = 0
        minLength = 0
        
        degree = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num not in degree:
                degree[num] = [i, 1]
            else:
                degree[num][1] += 1
            
            if degree[num][1] > maxFrequency:
                maxFrequency = degree[num][1]
                minLength = i - degree[num][0]
            
            elif degree[num][1] == maxFrequency:
                minLength = min(minLength, i - degree[num][0])
        
        return minLength + 1
    
    
