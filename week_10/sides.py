from typing import List


class Solution:
    def check(self, row, col, m, n):
        if 0 <= row < m and 0 <= col < n:
            return True

    def onBorder(self, row, col, m, n):
        if row == 0 or row == m - 1 or col == 0 or col == n - 1:
            return True

    def dfs(self, row, col, board, visited, DIR):

        if self.check(row, col, len(board), len(board[0])) and self.onBorder(row, col, len(board), len(board[0])) and board[row][col] == 'O':
            return True
        visited.append([row, col])
        sides = False

        for direction in DIR:
            newRow, newCol = row + direction[0], col + direction[1]

            if self.check(newRow, newCol, len(board), len(board[0])) and board[newRow][newCol] == 'X' and [newRow, newCol] not in visited:
                sides = sides or False
            elif self.check(newRow, newCol, len(board), len(board[0])) and board[newRow][newCol] == 'O' and [newRow, newCol] not in visited:
                sides = sides or self.dfs(newRow, newCol, board, visited, DIR)
        if not sides:
            board[row][col] = 'X'
        return sides

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' and not self.onBorder(row, col, len(board), len(board[0])):
                    print(row, col)
                    self.dfs(row, col, board, visited, DIR)
                    # for query in visited:
                    #     board[query[0]][query[1]] = 'X'
                    # print(row, col)
                    # visited = []

        print(board)


Solution().solve([["O", "O", "O", "O"], ["X", "O", "O", "X"],
                  ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
