class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False
        self.word = ""


class Trie:
    def __init__(self):
        self.head = TrieNode()
        self.head.isWordEnd = True

    def add(self, word: str):
        pointer = self.head

        for char in word:
            if char not in pointer.children:
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]

        pointer.isWordEnd = True
        pointer.word = word


class Solution:
    def traverse(self, node: TrieNode, canBeMadeFromExisitingWord: bool):
        if node.isWordEnd and canBeMadeFromExisitingWord:
            wordLength = len(node.word)
            self.maxLongestWord = max(wordLength, self.maxLongestWord)
            self.longestWords[wordLength].append(node.word)

        for child in node.children:
            self.traverse(
                node.children[child], canBeMadeFromExisitingWord and node.isWordEnd)

    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.add(word)

        self.longestWords = defaultdict(list)
        self.maxLongestWord = 0
        self.traverse(trie.head, True)

        if not self.longestWords:
            return ''

        longestWordFromHashMap = sorted(self.longestWords[self.maxLongestWord])

        return longestWordFromHashMap[0]
