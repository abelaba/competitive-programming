class Solution:   
    
    def racecar(self, target: int) -> int:
        
        # moves, position, speed
        queue = deque()
        queue.append([0, 0, 1])
        
        while queue:
            
            moves, position, speed = queue.popleft()
            
            if target == position:
                return moves
            
            queue.append((moves+1, position+speed, speed*2))
            
            if (position+speed > target and speed > 0) or (position+speed < target and speed < 0):
                
                speed = -1 if speed > 0 else 1
                queue.append((moves+1, position, speed))
                
                
            
            
            
            
            
            
            
