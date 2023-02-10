class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        
        onesA = []
        onesB = []
        
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                       onesA.append((i, j))
                
                if B[i][j] == 1:
                       onesB.append((i, j))

        count = defaultdict(int)
        maxCount = 0
        
        for x1, y1 in onesA:
            for x2, y2 in onesB:
                diff = (y2-y1, x2-x1)
                count[diff] += 1
                maxCount = max(maxCount, count[diff])
        
        return maxCount
                
                
        
