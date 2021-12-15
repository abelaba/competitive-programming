class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort()
        print(nums)
        for i in range(0, len(nums)):
            for j in range(0, len(nums) - 1):
                x1 = str(nums[j])*9
                x2 = str(nums[j+1])*9
                print(x1[:9])
                print(x2[:9])
                if(x1[:9] < x2[:9]):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                elif((x1[:9] == x2[:9])):
                    if(x1 < x2):
                        temp = nums[j]
                        nums[j] = nums[j+1]
                        nums[j+1] = temp

        while nums[0] == 0:
            if(len(nums) > 1):
                nums.pop(0)
            else:
                break
        return ''.join([str(elem) for elem in nums])
