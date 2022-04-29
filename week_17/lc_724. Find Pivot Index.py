class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        su_m = sum(nums)
        prefixSum = 0
        for i in range(len(nums)):
            if prefixSum == su_m - prefixSum - nums[i]:
                return i
            prefixSum += nums[i]

        return -1
