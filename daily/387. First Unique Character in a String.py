class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for i in range(len(s)):
            char = s[i]
            if count[char] == 1:
                return i
        return -1
        
