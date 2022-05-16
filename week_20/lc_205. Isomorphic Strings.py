class Solution:
    def check(self, s, t):
        letterMapping = {}
        stack = []
        for i in range(len(s)):
            if t[i] not in letterMapping:
                stack.append(s[i])
                letterMapping[t[i]] = s[i]
            else:
                stack.append(letterMapping[t[i]])
        return ''.join(stack) == s

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.check(s, t) and self.check(t, s)
