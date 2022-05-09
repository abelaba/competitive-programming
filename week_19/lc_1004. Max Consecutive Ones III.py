class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow = fast = maxNumbersOfOnes = flippedZeros = 0
        lengthOfNums = len(nums)

        while fast < lengthOfNums:
            if nums[fast] == 1:
                fast += 1
            elif nums[fast] == 0:
                if flippedZeros >= k:
                    while flippedZeros >= k:
                        if nums[slow] == 0:
                            flippedZeros -= 1
                        slow += 1
                else:
                    flippedZeros += 1
                    fast += 1
            maxNumbersOfOnes = max(maxNumbersOfOnes, fast - slow)
        return maxNumbersOfOnes
