class Solution:
    def sortSentence(self, s: str) -> str:
        stringArray = s.split(" ")
        frequency = [0] * len(stringArray)
        for i in stringArray:
            frequency[eval(i[-1])-1] = i[:-1]
        return ' '.join(frequency)
