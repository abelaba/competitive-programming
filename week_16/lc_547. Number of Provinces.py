# dfs and union find implementation
class Solution:
    def dfs(self, index):
        if index in self.visited:
            return

        self.visited.add(index)

        for child in self.graph[index]:
            self.dfs(child)

    def find(self, parent, x):
        root = x
        while root != parent[root]:
            root = parent[root]

        return root

    def union(self, parent, x, y):
        x_parent = self.find(parent, x)
        y_parent = self.find(parent, y)
        parent[x_parent] = y_parent

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        self.graph = {}
        count = 0
        length = len(isConnected)

        for i in range(length):
            for j in range(length):
                if i not in self.graph:
                    self.graph[i] = []
                if isConnected[i][j] == 1 and i < j:
                    self.graph[i].append(j)

#         for i in self.graph:
#             if i not in self.visited:
#                 self.dfs(i)

#                 count += 1
#         return count

        parent = [x for x in range(length)]

        for i in range(length):
            for child in self.graph[i]:
                self.union(parent, child, i)

        for i in range(length):
            parent[i] = self.find(parent, i)

        parent = set(parent)

        return len(parent)
