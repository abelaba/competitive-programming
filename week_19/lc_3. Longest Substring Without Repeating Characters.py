class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = fast = maximumSize = 0
        lengthOfString = len(s)
        charsInWindow = defaultdict(int)

        while fast < lengthOfString:
            letterOnFastPointer = s[fast]
            if charsInWindow[letterOnFastPointer] == 0:
                charsInWindow[letterOnFastPointer] += 1
                fast += 1
            else:
                while charsInWindow[letterOnFastPointer] > 0:
                    letterOnSlowPointer = s[slow]
                    if charsInWindow[letterOnSlowPointer] > 0:
                        charsInWindow[letterOnSlowPointer] -= 1
                    slow += 1
            windowSize = fast - slow
            maximumSize = max(maximumSize, windowSize)

        return maximumSize
