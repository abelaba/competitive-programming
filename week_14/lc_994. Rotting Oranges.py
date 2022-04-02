class Solution:
    def check(self, row, col, m, n):
        if 0 <= row < m and 0 <= col < n:
            return True

    def orangesRotting(self, grid: List[List[int]]) -> int:

        length = len(grid)
        width = len(grid[0])

        DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        queue = collections.deque([])
        freshOranges = 0
        minutes = 0

        # Find all rotten oranges and fresh tomatoes

        for row in range(length):
            for col in range(width):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    freshOranges += 1

        while queue and freshOranges > 0:
            minutes += 1
            print(queue)
            for i in range(len(queue)):
                row, col = queue.popleft()

                for direction in DIR:
                    newRow, newCol = row + direction[0], col + direction[1]

                    if self.check(newRow, newCol, length, width) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        freshOranges -= 1

        if freshOranges > 0:
            return -1

        return minutes
