class Solution:
    
    def findLetter(self, string, stack, answer, index):
        
        if index == len(string): 
            answer.append(''.join(stack))
            return
        
        # If character is number
        if string[index].isdigit():
            stack.append(string[index])
            self.findLetter(string, stack, answer, index + 1)
            stack.pop()
        
        # If character is an alphabet
        else:
            stack.append(string[index].lower())
            self.findLetter(string, stack, answer, index + 1)
            stack.pop()
            
            stack.append(string[index].upper())
            self.findLetter(string, stack, answer, index + 1)
            stack.pop()
        
    
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        self.findLetter(s, [], answer, 0)
        return answer
        
        