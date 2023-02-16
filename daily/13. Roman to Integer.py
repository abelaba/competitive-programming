class Solution:
    def romanToInt(self, s: str) -> int:
        romanSymbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        prev = "M"
        for i in range(len(s)):
            letter = s[i]
            if romanSymbols[prev] >= romanSymbols[letter]:
                number += romanSymbols[letter]
            else:
                number += romanSymbols[letter] - (2 * romanSymbols[prev])
            prev = letter
        return number
