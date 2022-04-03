class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(0, len(matrix)):
            left, right = 0, len(matrix[0]) - 1

            if target <= matrix[i][right]:

                while left <= right:
                    middle = left + (right - left) // 2
                    middlElement = matrix[i][middle]

                    if target > middlElement:
                        left = middle + 1
                    elif target < middlElement:
                        right = middle - 1
                    else:
                        return True
