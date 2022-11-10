class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        mask = 0
        answer = []
        
        for num in nums:
            shift = 1 << num
            if shift & mask != 0:
                answer.append(num)
            
            mask |= shift
        
        for i in range(1, len(nums) + 1):
            shift = 1 << i
            if shift & mask == 0:
                answer.append(i)
                return answer
        
            
        
        
        
        