class Solution:
    def check(self, row, col, m, n):
        if 0 <= row < m and 0 <= col < n:
            return True

    def traverse(self, row, col, grid, DIR):

        grid[row][col] = 0
        count = 1

        for direction in DIR:
            newRow = row + direction[0]
            newCol = col + direction[1]

            if self.check(newRow, newCol, len(grid), len(grid[0])) and grid[newRow][newCol] == 1:
                count += self.traverse(newRow, newCol, grid, DIR)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ma_x = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count = self.traverse(row, col, grid, DIR)
                    ma_x = max(ma_x, count)
        return ma_x
