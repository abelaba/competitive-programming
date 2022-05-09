class Solution:
    def decoder(self, word: str, stack: List, index: int, nums: set) -> List:
        if index == len(word):
            return
        if word[index] == "]":
            letter = deque()
            while stack[-1] != "[":
                letter.appendleft(stack.pop())
            stack.pop() # Remove "]" from stack
            
            number = ""
            while stack and stack[-1] in nums:
                number += stack.pop()
            repeatedWord = int(number[::-1]) * ''.join(letter)
            stack.append(repeatedWord)
                
        else:
            stack.append(word[index])
        self.decoder(word, stack, index + 1, nums)
        
        
    def decodeString(self, s: str) -> str:
        numbers = {"0","1","2","3","4","5","6","7","8","9"}
        stack = []
        self.decoder(s, stack, 0, numbers)
        
        
        return ''.join(stack)
