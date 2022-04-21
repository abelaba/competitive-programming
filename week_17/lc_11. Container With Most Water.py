class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        left = 0
        right = len(height) - 1

        while left < right:
            leftHeight = height[left]
            rightHeight = height[right]

            container = min(leftHeight, rightHeight) * (right - left)
            maxArea = max(maxArea, container)

            if leftHeight < rightHeight:
                left += 1
            else:
                right -= 1

        return maxArea
