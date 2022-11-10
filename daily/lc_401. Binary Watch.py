class Solution:
    
    def convert(self, bits):
        hour = 0
        minutes = 0
        for bit in bits:
            if bit >= 6:
                x = 1 << bit - 6
                hour ^= x
            else:
                x = 1 << bit
                minutes ^= x
                
        if hour > 11 or minutes > 59:
            return None
        minutes = str(minutes) if minutes >= 10 else "0" + str(minutes)
        return str(hour) + ":" +  minutes
    
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        answer = []
        stack = []
        
        def binary(k, index):
            if k == 0: 
                time = self.convert(stack)
                if time:
                    answer.append(time)
                return
            
            for i in range(index + 1, 11):
                stack.append(i - 1)
                binary(k - 1, i)
                stack.pop()
        
        binary(turnedOn, 0)
        return answer
                
                
        
            
            
            