class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        
        letterCount = {}
        for letter in s:
            if letter in letterCount:
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1
        
        stack = []

        for letter in s:
            if len(stack) == 0:
                stack.append(letter)

            while stack and stack[-1] > letter and letterCount[stack[-1]] > 0 and letter not in stack:
                stack.pop()
                
            if letter not in stack:
                stack.append(letter)
                
            letterCount[letter] -= 1

        return ''.join(stack)
                