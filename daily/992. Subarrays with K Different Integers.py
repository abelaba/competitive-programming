class Solution:
    
    def findSubArrays(self, nums, k):
        count = defaultdict(int)
        
        left = 0
        right = 0
        answer = 0
        
        numbers = 0
                
        while right < len(nums):
            
            if not count[nums[right]]:
                numbers += 1
                
            count[nums[right]] += 1
            
            
            while numbers > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    numbers -= 1
                
                left += 1

            answer += right - left + 1
            right += 1
        
        return answer
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        
        return self.findSubArrays(nums, k) - self.findSubArrays(nums, k-1)
