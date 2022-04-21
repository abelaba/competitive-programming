class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = 1
        freq = 1
        su_m = nums[left]

        while right < len(nums):
            su_m += nums[right]

            while su_m + k < nums[right] * (right - left + 1):
                su_m -= nums[left]
                left += 1

            freq = max(freq, (right - left + 1))

            right += 1

        return freq
