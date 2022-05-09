class Solution:
    def addValues(self, chars: List[str], count: int, index: int, slow: int) -> int:
        chars[index] = chars[slow]
        index += 1
        if count > 1:
            count = str(count)
            for digit in count:
                chars[index] = digit
                index += 1
        return index

    def compress(self, chars: List[str]) -> int:
        slow = fast = count = index = 0
        length = len(chars)

        while fast < length:
            if chars[slow] == chars[fast]:
                count += 1
                if fast == length - 1:
                    index = self.addValues(chars, count, index, slow)
                fast += 1

            elif chars[slow] != chars[fast]:
                index = self.addValues(chars, count, index, slow)
                count = 0
                slow = fast

        return index
