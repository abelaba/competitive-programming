class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        floor = len(nums)//3
        array = []
        appearance = 0
        num = nums[0]
        print(nums)
        appended = False

        for j in range(0, len(nums)):
            print(f" num{num} app{appearance} ")
            if(num == nums[j]):
                appearance += 1
            elif(num != nums[j]):
                appearance = 1
                num = nums[j]
                appended = False
            if(appearance > floor and not appended):
                array.append(num)
                appended = True

        return array
