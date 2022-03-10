def binarySearch(choice, nums, target):
    left = 0
    right = len(nums) - 1

    appearance = -1

    while left <= right:
        middle = int(left + (right - left) / 2)
        if nums[middle] == target:
            appearance = middle
            if choice == "first":
                right = middle - 1
            elif choice == "last":
                left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1

    return appearance


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        firstAppearance = binarySearch("first", nums, target)
        lastAppearance = binarySearch("last", nums, target)

        return [firstAppearance, lastAppearance]
