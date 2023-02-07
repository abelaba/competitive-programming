class Solution:
    
    def justify(self, section, maxWidth, isLastString):
        
        words, wordLength = section
        
        n = len(words)-1
        
        spaceLeft = maxWidth-wordLength
        
        if n == 0:
            return words[-1] + ' '*spaceLeft
        
        if isLastString:
            string = ' '.join(words)
            string += ' '*(spaceLeft - n)
            
                
        elif spaceLeft % n == 0:
            space = spaceLeft // n
            string = ' '*space
            string = string.join(words)
        
        else:
            extraSpace = spaceLeft % n
            space = spaceLeft // n
            temp = []
            
            for i in range(n):
                temp.append(words[i])
                
                if extraSpace:
                    temp.append(' '*space + ' ')
                    extraSpace -= 1
                else:
                    temp.append(' '*space)
            
            temp.append(words[-1])
            
            string = ''.join(temp)
            
            
        
        return string
        
            
    
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        
        answer = []
        
        letterCount = 0
        
        temp = []
        
        for word in words:
            
            if letterCount + len(temp) + len(word) <= maxWidth:
                letterCount += len(word)
                temp.append(word)
            
            else:
                answer.append([temp.copy(), letterCount])
                temp = [word]
                
                letterCount = len(word)
        
        answer.append([temp.copy(), letterCount])
        
        
        for i in range(len(answer)):
            section = answer[i]
            justified = self.justify(section, maxWidth, i==len(answer)-1)
            answer[i] = justified
            
        
        return answer
    
