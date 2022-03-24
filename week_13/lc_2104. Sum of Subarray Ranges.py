class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        su_m = 0
        length = len(nums)

        for index in range(0, length):

            maximum = minimum = nums[index]

            for j in range(index + 1, length):
                num = nums[j]
                if num < minimum:
                    minimum = num
                elif num > maximum:
                    maximum = num

                su_m += maximum - minimum

        return su_m
