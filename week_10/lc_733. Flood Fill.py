class Solution:
    def check(self,row,col,m,n):
        if 0 <= row < m and 0 <= col < n:
            return True
    def dfs(self,image,DIR,row,col,newColor,removedColor,visited):

        image[row][col] = newColor
        visited.append([row,col])
        for element in DIR:
            newRow = element[0] + row
            newCol = element[1] + col

            if not self.check(newRow,newCol,len(image),len(image[0])) or [newRow,newCol] in visited or image[newRow][newCol] != removedColor:
                continue    
            self.dfs(image,DIR,newRow,newCol,newColor,removedColor,visited)
            
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        removedColor = image[sr][sc]
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = []
        self.dfs(image,DIR,sr,sc,newColor,removedColor,visited)
        return image      
       
        
        