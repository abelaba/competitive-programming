class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        left = 1
        right = len(nums) - 1
        answer = 0

        while left <= right:

            mid = left + (right - left) // 2
            count = 0

            for num in nums:
                if num <= mid:
                    count += 1
            print(count, mid, nums[mid])
            if count > mid:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
