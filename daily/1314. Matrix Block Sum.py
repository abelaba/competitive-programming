class Solution:

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0])
        
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = mat[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        
        ans = [[0 for _ in range(cols)] for _ in range(rows)]
        
        
        for i in range(rows):
            for j in range(cols):
                
                r1, r2 = max(0, i-k), min(rows-1, i+k)
                c1, c2 = max(0, j-k), min(cols-1, j+k)
                
                ans[i][j] = dp[r2+1][c2+1]
                
                if r1 > 0:
                    ans[i][j] -= dp[r1][c2+1]
                
                if c1 > 0:
                    ans[i][j] -= dp[r2+1][c1]
                
                if r1 > 0 and c1 > 0:
                    ans[i][j] += dp[r1][c1]
        
        return ans
        
        
                
                
                
                
                
                
                
                
                
                
