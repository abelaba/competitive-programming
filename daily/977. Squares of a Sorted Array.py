class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        for i in nums:
            array.append(i*i)
        array.sort()
        
        return array
            
        
