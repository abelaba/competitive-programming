class Solution:
    def findMinimumPathSum(self, level, index, triangle, memo):

        if (level, index) in memo:
            return memo[(level, index)]

        if level == len(triangle) - 1:
            return triangle[level][index]

        left = triangle[level][index] + \
            self.findMinimumPathSum(level + 1, index, triangle, memo)
        right = triangle[level][index] + \
            self.findMinimumPathSum(level + 1, index + 1, triangle, memo)

        memo[(level, index)] = min(left, right)

        return memo[(level, index)]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        return self.findMinimumPathSum(0, 0, triangle, memo)
