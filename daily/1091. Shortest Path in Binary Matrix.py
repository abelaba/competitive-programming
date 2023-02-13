class Solution:
    # V = Vertices
    # E = Edges
    # Time Complexity -> O(V + E)
    # Space Complexity -> O(V)
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return - 1
        
        DIR = [[0,1],[1,0],[-1,0],[0,-1],[-1,1],[1,-1],[-1,-1],[1,1]]
        
        length = len(grid)
        width = len(grid[0])
        
        visited = {(0,0)}
        queue = collections.deque([((0, 0), 1)])        
        
        while queue:
            (row, col), weight = queue.popleft()
            
            if row == length - 1 and col == width - 1 and grid[row][col] == 0:
                return weight
            
            for x, y in DIR:
                newRow, newCol = x + row, y + col
                if  0 <= newRow < length and 0 <= newCol < width:
                    if (newRow, newCol) not in visited and grid[newRow][newCol] == 0:
                        visited.add((newRow,newCol))
                        queue.append(((newRow, newCol), weight + 1))
            
        return -1
        
        
        
        
