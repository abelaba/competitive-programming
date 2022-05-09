class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str):
        pointer = self.root
        for ch in word:
            if ch not in pointer.children:
                pointer.children[ch] = TrieNode()
            pointer = pointer.children[ch]
        pointer.isWordEnd = True
        pointer.count += 1


class Solution:

    def traverse(self, apperance: List[str], node: TrieNode(), index: int):
        if node.isWordEnd:
            self.count += node.count
        for adj in node.children:
            if adj in apperance:
                found = -1
                left = 0
                right = len(apperance[adj]) - 1
                a = apperance[adj]

                while left <= right:
                    middle = left + (right - left) // 2
                    if a[middle] >= index:
                        found = a[middle]
                        right = middle - 1
                    else:
                        left = middle + 1

                if found != -1:
                    child = node.children[adj]
                    self.traverse(apperance, child, found + 1)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.add(word)
        self.count = 0

        letterAppearance = defaultdict(list)
        length = len(s)

        for i in range(length):
            letter = s[i]
            letterAppearance[letter].append(i)

        self.traverse(letterAppearance, trie.root, 0)

        return self.count
