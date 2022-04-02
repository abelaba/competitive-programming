
class Solution:
    def check(self, row, col, m, n):
        if 0 <= row < m and 0 <= col < n:
            return True

    def onBorder(self, row, col, m, n):
        if row == 0 or row == m - 1 or col == 0 or col == n - 1:
            return True

    def dfs(self, row, col, board, visited, DIR, length, width):

        visited.add((row, col))
                
        for direction in DIR:
            newRow, newCol = row + direction[0], col + direction[1]

            if self.check(newRow, newCol, length, width): 
                b = board[newRow][newCol]
                
                if b == 'O' and (newRow, newCol) not in visited:
                    self.dfs(newRow, newCol, board, visited, DIR, length, width)
        

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        length = len(board)
        width = len(board[0])
        
        for row in range(length):
            for col in range(width):
                if (row, col) not in visited and board[row][col] == 'O' and self.onBorder(row, col, length, width):
                    self.dfs(row, col, board, visited, DIR, length, width)
        
        for row in range(length):
            for col in range(width):
                if (row, col) not in visited and board[row][col] == 'O':
                    board[row][col] = 'X'
                    
 
