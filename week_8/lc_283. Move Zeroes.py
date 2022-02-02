class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        slow = 0
        fast = len(nums) - 1
        while slow < fast:
            if nums[slow] == 0:
                zero = nums.pop(slow)
                nums.append(zero)
                fast -= 1
            else:
                slow += 1
