class Solution:
    
    def findSlope(self, x1, y1, x2, y2):
        # m = (y2 - y1) / (x2 - x1)
        # y = mx + b, b = y - mx
        if x2 - x1 == 0:
            return x2
        
        m = (y2-y1) / (x2-x1)
        
        b = y1 - (m*x1)
        
        return (m, b)
        
    def maxPoints(self, points: List[List[int]]) -> int:
        
        lines = defaultdict(set)
        
        maxPointsOnALine = 1
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                
                line = self.findSlope(x1, y1, x2, y2)
                lines[line].add((x1, y1))
                lines[line].add((x2, y2))
                
                maxPointsOnALine = max(maxPointsOnALine, len(lines[line]))
        
        return maxPointsOnALine