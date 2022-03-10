class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negativeNumbers = 0
        for row in range(0, len(grid)):
            left = 0
            right = len(grid[0]) - 1
            while left <= right:
                middle = left + (right - left) // 2
                if grid[row][middle] >= 0:
                    left = middle + 1
                elif grid[row][middle] < 0:
                    # print(right,middle,left,negativeNumbers)
                    negativeNumbers += right - middle + 1
                    right = middle - 1

        return negativeNumbers
