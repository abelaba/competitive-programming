class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            middlElement = nums[mid]
            leftElement = nums[left]

            if target == middlElement:
                return mid

            elif middlElement >= leftElement:
                if leftElement <= target <= middlElement:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                rightElement = nums[right]
                if middlElement <= target <= rightElement:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
