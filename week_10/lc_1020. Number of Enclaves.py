class Solution:
    def check(self, row, col, m, n):
        if 0 <= row < m and 0 <= col < n:
            return True

    def onBorder(self, row, col, m, n):
        if row == 0 or row == m - 1 or col == 0 or col == n - 1:
            return True

    def searchWalkableLand(self, row, col, visited, grid, DIR):

        if self.check(row, col, len(grid), len(grid[0])) and self.onBorder(row, col, len(grid), len(grid[0])) and grid[row][col] == 1:
            return 0

        visited.add((row, col))
        walkableLand = []
        for direction in DIR:
            newRow, newCol = row + direction[0], col + direction[1]

            if self.check(newRow, newCol, len(grid), len(grid[0])) and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                walkableLand.append(self.searchWalkableLand(
                    newRow, newCol, visited, grid, DIR))

        if 0 in walkableLand:
            return 0
        else:
            walkableLand.append(1)
            return sum(walkableLand)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        walkableLand = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    walkableLand += self.searchWalkableLand(
                        row, col, visited, grid, DIR)
                    # print(row,col,walkableLand,visited)
                    # return

        return walkableLand
