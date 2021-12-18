class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        length = int(len(nums) / 2)
        left = 0
        right = -1
        maximum = 0
        for i in range(length):
            maximum = max(maximum, nums[left] + nums[right])
            left += 1
            right -= 1
        return maximum
