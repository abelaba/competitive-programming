class Solution:
    def isValid(self, matrix, row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == "1"
    
    def find(self, memo, maxVal, matrix, row, col):
        state = (row, col)
        
        if state in memo:
            return memo[state]
        
        if not self.isValid(matrix, row, col):
            memo[state] = 0
            return memo[state]

        temp = sys.maxsize
        
        for x, y in self.directions:
            newRow, newCol = row+x, col+y
            rec = self.find(memo, maxVal, matrix, newRow, newCol)
            temp = min(temp, rec)
        
        memo[state] = temp + 1
        
        maxVal[0] = max(maxVal[0], memo[state])
        
        return memo[state]
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
                
        self.directions = [(1, 0), (0, 1), (1, 1)]
        
        maxVal = [0]
        memo = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.find(memo, maxVal, matrix, i ,j)
        
        return maxVal[0]**2
