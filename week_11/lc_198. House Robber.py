class Solution:
    def findMaxLoot(self, index, nums, memo):

        if index in memo:
            return memo[index]

        if index >= len(nums):
            return 0

        if index == len(nums) - 1 or index == len(nums) - 2:
            return nums[index]

        jump2 = self.findMaxLoot(index + 2, nums, memo)
        jump3 = self.findMaxLoot(index + 3, nums, memo)

        memo[index] = nums[index] + max(jump2, jump3)

        return memo[index]

    def rob(self, nums: List[int]) -> int:
        memo = {}
        maxLoot = 0
        for index in range(len(nums)):
            maxLoot = max(maxLoot, self.findMaxLoot(index, nums, memo))

        return maxLoot
