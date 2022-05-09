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
    def findMatchingWords(self, node: TrieNode, pattern: str, index: int, wordsThatMatchPattern: set):
        if node.isWordEnd and index == len(pattern):
            wordsThatMatchPattern.add(node.word)

        for child in node.children:
            if index < len(pattern) and child == pattern[index]:
                self.findMatchingWords(
                    node.children[child], pattern, index + 1, wordsThatMatchPattern)
            else:
                isLowerCase = ord(child) >= ord("a")
                if isLowerCase:
                    self.findMatchingWords(
                        node.children[child], pattern, index, wordsThatMatchPattern)

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie = Trie()
        for query in queries:
            trie.add(query)
        wordsThatMatchPattern = set()
        self.findMatchingWords(trie.head, pattern, 0, wordsThatMatchPattern)

        answer = []
        for query in queries:
            answer.append(query in wordsThatMatchPattern)

        return answer
