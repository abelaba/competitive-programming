class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLength = len(needle)
        hayLength = len(haystack)

        for i in range(len(haystack)):
            hay = haystack[i]
            if hay == needle[0]:
                index = 0
                j = i
                while j < hayLength and index < needleLength and haystack[j] == needle[index]:
                    index += 1
                    j += 1
                if index == needleLength:
                    return i
        return -1
