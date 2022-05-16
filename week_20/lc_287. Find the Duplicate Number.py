class Solution:
    # Bit Manipulation  left shift then or
    def findDuplicate(self, nums: List[int]) -> int:
        num = 0
        for k in nums:
            leftShift = 1 << k
            if num & leftShift != 0:
                return k
            num |= leftShift
