from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dictionary = {}

        for index in range(len(s)):
            letter = s[index]
            if letter in dictionary:
                dictionary[letter].append(index)
            else:
                dictionary[letter] = [index]

        parts = []
        ma_x = 0

        for letter in dictionary:
            firstAppearance = dictionary[letter][0]
            lastAppearance = dictionary[letter][-1]

            if firstAppearance <= ma_x:
                if lastAppearance > ma_x:
                    ma_x = lastAppearance
            else:
                parts.append(ma_x - sum(parts) + 1)
                ma_x = lastAppearance

        parts.append(ma_x - sum(parts) + 1)

        return parts
