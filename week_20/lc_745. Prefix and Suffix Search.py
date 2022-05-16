class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False
        self.index = -1
        self.word = ''


class Trie:
    def __init__(self):
        self.head = TrieNode()
        self.head.isWordEnd = True

    def add(self, word: str, index: int):
        pointer = self.head

        for char in word:
            if char not in pointer.children:
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]

        pointer.isWordEnd = True
        pointer.index = index
        pointer.word = word[::-1]


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i in range(len(words)):
            word = words[i]
            self.trie.add(word, i)

    def search(self, node: TrieNode, prefix, index, suffix):
        if node.isWordEnd:
            suffixLength = len(suffix)
            if suffix == node.word[:suffixLength]:
                self.maxIndex = max(self.maxIndex, node.index)

        for child in node.children:
            if index < len(prefix) and child == prefix[index]:
                self.search(node.children[child], prefix, index + 1, suffix)
            elif index == len(prefix):
                self.search(node.children[child], prefix, index, suffix)

    def f(self, prefix: str, suffix: str) -> int:
        self.maxIndex = -1
        self.search(self.trie.head, prefix, 0, suffix[::-1])
        return self.maxIndex


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
