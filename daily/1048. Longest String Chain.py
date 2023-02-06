class Solution:
    def traverse(self, index, predecessor, wordLength):
        if predecessor in self.cache:
            return self.cache[predecessor]
        
        if index not in wordLength:
            return 0
        
        maxCount = 0
        
        for word in wordLength[index]:
            for i in range(index + 1):
                checkWord = word[:i] + word[i+1:]
                if checkWord == predecessor:
                    count = self.traverse(index + 1, word, wordLength)
                    maxCount = max(count + 1, maxCount)
                    break
        
        self.cache[predecessor] = maxCount       
        return maxCount
        
    def longestStrChain(self, words: List[str]) -> int:
        wordLength = defaultdict(list)
        for word in words:
            wordLength[len(word)].append(word)
        
        self.cache = {}
        longestChain = 0
        
        for index in sorted(wordLength.keys()):
            for word in wordLength[index]:
                chain = self.traverse(index + 1, word, wordLength)
                longestChain = max(chain, longestChain)
        
        return longestChain + 1
        
        
