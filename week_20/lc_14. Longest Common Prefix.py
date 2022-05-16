class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)

        stack = [char for char in strs[0]]
        prefixIndex = len(stack)

        for i in range(1, len(strs)):
            string = strs[i]
            for j in range(len(string)):
                if j == prefixIndex:
                    break
                if stack[j] != string[j]:
                    prefixIndex = j
                    break

        return ''.join(stack[:prefixIndex])
