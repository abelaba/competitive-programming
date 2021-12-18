class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boolArray = []
        for i in range(len(l)):
            subArray = nums[l[i]:r[i]+1]
            subArray.sort()
            boolean = True
            for i in range(0, len(subArray) - 1):
                firstDifference = subArray[1] - subArray[0]
                if(subArray[i+1] - subArray[i] != firstDifference):
                    boolean = False
                    break
            boolArray.append(boolean)
        return boolArray
