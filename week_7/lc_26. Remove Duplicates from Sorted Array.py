class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                nums.pop(fast)
            else:
                slow += 1
                fast += 1
