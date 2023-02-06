class Solution:
    
    def check(self, word, prefix):
        
        if len(prefix) > len(word):
            return False
        
        for i in range(len(prefix)):
            
            if word[i] != prefix[i]:
                return False
            
        return True
        
    
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0
        
        for word in words:
            isPrefix = self.check(word, pref)
            count += int(isPrefix)
        
        return count
        
        
