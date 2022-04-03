class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        answer = 1

        while left <= right:
            middle = left + (right - left) // 2

            t = 0
            for num in nums:
                t += math.ceil(num / middle)

            if t > threshold:
                left = middle + 1
            else:
                answer = middle
                right = middle - 1

        return answer
