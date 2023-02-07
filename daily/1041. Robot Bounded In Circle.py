class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        instructions = 4*instructions
        
        start = [0, 0]
        
        position = [0, 0]
        
        x, y = 0, 1
        
        for instruction in instructions:
            if instruction == "G":
                position[0] += x
                position[1] += y
            
            elif instruction == "L":
                x, y = -y, x
            
            elif instruction == "R":
                x, y = y, -x
        
        return position == start
