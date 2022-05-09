class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def add(self, word: str):
        pointer = self.head

        for i in range(len(word) - 1, -1, -1):
            letter = word[i]
            if letter not in pointer.children:
                pointer.children[letter] = TrieNode()
            pointer = pointer.children[letter]

        pointer.isEnd = True


class Solution:
    def traverse(self, node, count):
        if not node.children and node.isEnd:
            self.count += count + 1

        for child in node.children:
            self.traverse(node.children[child], count + 1)

    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.add(word)

        self.count = 0
        self.traverse(trie.head, 0)

        return self.count
