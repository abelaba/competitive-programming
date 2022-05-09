class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        pointer = self.head
        for char in word:
            if char not in pointer.children:
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]
        pointer.isWordEnd = True

    def search(self, word: str, index: int = 0, node: TrieNode = None) -> bool:
        if not node:
            node = self.head

        if node.isWordEnd and index == len(word):
            return True
        elif index == len(word):
            return False

        for child in node.children:
            if word[index] == ".":
                if self.search(word, index + 1, node.children[child]):
                    return True
            elif word[index] == child:
                return self.search(word, index + 1, node.children[child])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
