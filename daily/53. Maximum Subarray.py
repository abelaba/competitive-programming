class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        N = len(nums)
        SumMax = nums[0]
        curentSum = 0
        
        for i in range(N):
            if curentSum<0:
                curentSum = 0
            curentSum += nums[i]
            if curentSum > SumMax:
                SumMax = curentSum
        return SumMax
