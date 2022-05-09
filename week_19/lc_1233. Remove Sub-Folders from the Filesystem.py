class TrieNode:
    def __init__(self):
        self.children = {}
        self.isFolder = False
        self.path = ""


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def add(self, folderPath: str):
        folder = folderPath
        folderPath = folderPath.split("/")

        pointer = self.head
        for folderName in folderPath:
            if folderName == "":
                continue
            if folderName not in pointer.children:
                pointer.children[folderName] = TrieNode()
            pointer = pointer.children[folderName]

        pointer.path = folder
        pointer.isFolder = True


class Solution:
    def traverse(self, node: TrieNode, mainFolders: List[str]):
        if node.isFolder:
            mainFolders.append(node.path)
            return
        for child in node.children:
            self.traverse(node.children[child], mainFolders)

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for folderName in folder:
            trie.add(folderName)

        mainFolders = []
        self.traverse(trie.head, mainFolders)

        return mainFolders
