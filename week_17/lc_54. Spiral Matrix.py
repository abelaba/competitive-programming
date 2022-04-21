class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        row = len(matrix)
        column = len(matrix[0])
        x = 0

        spiral = []
        totalElements = row * column

        while len(spiral) != totalElements:

            for i in range(x, column):
                spiral.append(matrix[x][i])

            for i in range(x+1, row):
                spiral.append(matrix[i][column - 1])

            if len(spiral) == totalElements:
                break

            for i in range(column - 2, x - 1, -1):
                spiral.append(matrix[row - 1][i])

            for i in range(row - 2, x, -1):
                spiral.append(matrix[i][x])

            x += 1
            row -= 1
            column -= 1

        return spiral
