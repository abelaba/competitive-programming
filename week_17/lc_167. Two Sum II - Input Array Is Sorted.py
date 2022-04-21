class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left <= right:
            su_m = numbers[left] + numbers[right]
            if su_m < target:
                left += 1
            elif su_m > target:
                right -= 1
            else:
                return [left + 1, right + 1]
