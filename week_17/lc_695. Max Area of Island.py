# union find
class Solution:

    def find(self, parent, x):
        if parent[x] == x:
            return x
        return self.find(parent, parent[x])

    def union(self, parent, x, y, rank):
        x_parent = self.find(parent, x)
        y_parent = self.find(parent, y)

        if x_parent == y_parent:
            return

        if rank[x_parent] > rank[y_parent]:
            parent[y_parent] = x_parent
            rank[x_parent] += rank[y_parent]
            rank[y_parent] = 0

        elif rank[x_parent] <= rank[y_parent]:
            parent[x_parent] = y_parent
            rank[y_parent] += rank[x_parent]
            rank[x_parent] = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rowLength = len(grid)
        colLength = len(grid[0])

        rank = {}
        parent = {}

        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == 1:
                    parent[(i, j)] = (i, j)
                    rank[(i, j)] = 1

        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == 1:
                    if row - 1 >= 0 and grid[row - 1][col] == 1:
                        self.union(parent, (row, col), (row - 1, col), rank)

                    if col - 1 >= 0 and grid[row][col - 1] == 1:
                        self.union(parent, (row, col), (row, col - 1), rank)

        values = rank.values()

        if values:
            return max(rank.values())
        return 0
