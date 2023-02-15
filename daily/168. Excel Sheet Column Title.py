class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        stack = []
        while columnNumber != 0:
            stack.append(chr((columnNumber - 1) % 26 + ord('A')))
            columnNumber = (columnNumber - 1 ) // 26

        return ''.join(stack[::-1])
