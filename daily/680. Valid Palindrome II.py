class Solution:
    def check(self, string, left, right, removed):
        
        if left >= right:
            return True
        
        if string[left] == string[right]:
            return self.check(string, left + 1, right - 1, removed)
        
        elif not removed and string[left] != string[right]:
            return self.check(string, left + 1, right, True) or self.check(string, left, right - 1, True)
        
        return False
        
        
        
    def validPalindrome(self, s: str) -> bool:
        return self.check(s, 0, len(s) - 1, False)
