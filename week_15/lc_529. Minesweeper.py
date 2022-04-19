class Solution:
    def check(self, row, col, n, m):
        if 0 <= row < n and 0 <= col < m:
            return True

    def dfs(self, board, row, col, visited):

        visited.add((row, col))
        adjecentMines = 0

        for r, c in self.DIR:
            newRow, newCol = row + r, col + c
            if self.check(newRow, newCol, self.length, self.width):
                if board[newRow][newCol] == 'M':
                    adjecentMines += 1

        if adjecentMines > 0 and board[row][col] == 'E':
            board[row][col] = str(adjecentMines)
        elif adjecentMines == 0 and board[row][col] == 'E':
            board[row][col] = 'B'

        if board[row][col] == 'B':
            for r, c in self.DIR:
                newRow, newCol = row + r, col + c
                if self.check(newRow, newCol, self.length, self.width):
                    if (newRow, newCol) not in visited:
                        self.dfs(board, newRow, newCol, visited)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited = set()
        self.length = len(board)
        self.width = len(board[0])
        self.DIR = [[0, 1], [1, 0], [-1, 0], [0, -1],
                    [1, 1], [-1, 1], [1, -1], [-1, -1]]

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        self.dfs(board, click[0], click[1], visited)

        return board
