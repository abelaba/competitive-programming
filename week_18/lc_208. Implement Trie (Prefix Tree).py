class Node:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        pointer = self.root
        for char in word:
            if char not in pointer.children:
                pointer.children[char] = Node()
            pointer = pointer.children[char]
        pointer.isWordEnd = True

    def search(self, word: str, isPrefix: bool = False) -> bool:
        pointer = self.root

        for char in word:
            if char not in pointer.children:
                return False
            pointer = pointer.children[char]

        return pointer.isWordEnd or isPrefix

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
