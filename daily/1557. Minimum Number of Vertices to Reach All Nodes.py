class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        hasParent = [False] * n
        for start, end in edges:
            hasParent[end] = True
        res = []
        for i in range(n):
            if not hasParent[i]:
                res.append(i)
        return res
        
            
