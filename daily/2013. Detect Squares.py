class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)
          

    def add(self, point):
        x, y = point
        
        self.points[(x, y)] += 1
        
        
    def count(self, point):
        x, y = point
        
        squares = 0
        
        for x2, y2 in self.points.copy():
            
            if x2 == x and y != y2: 
                
                firstPoint = self.points[(x, y2)]
                diff = y2 - y
                
                newX = x + diff
                if (newX, y) in self.points and (newX, y2) in self.points:
                    squares += firstPoint * self.points[(newX, y)] * self.points[(newX, y2)]
                
                newX = x - diff
                if (newX, y) in self.points and (newX, y2) in self.points:
                    squares += firstPoint * self.points[(newX, y)] * self.points[(newX, y2)]
        
        return squares
