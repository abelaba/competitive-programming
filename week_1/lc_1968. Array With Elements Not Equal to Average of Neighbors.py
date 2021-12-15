# check if the numsbers are less than the median and if they are assign them to the odd index
import statistics


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        median = statistics.median(nums)
        even = 0
        odd = 1
        array = [0] * len(nums)
        for i in nums:
            if(i < median):
                array[odd] = i
                odd += 2
            else:
                array[even] = i
                even += 2
        return array
