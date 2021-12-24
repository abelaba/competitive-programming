class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monoStack = [nums2[0]]
        dictionary = {}
        for i in range(0, len(nums2)):
            while(nums2[i] > monoStack[-1]):
                ele = monoStack.pop()
                dictionary[ele] = nums2[i]
                if(len(monoStack) == 0):
                    monoStack.append(nums2[i])

            if(nums2[i] <= monoStack[-1]):
                dictionary[(nums2[i])] = -1
                monoStack.append(nums2[i])
        list = []
        for i in nums1:
            list.append(dictionary[i])
        return list
