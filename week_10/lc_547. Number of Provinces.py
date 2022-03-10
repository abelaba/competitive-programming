from typing import List


class Solution:
    def dfs(self, index):
        if index in self.visited:
            return
        self.visited.add(index)

        for child in self.graph[index]:
            self.dfs(child)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()

        self.graph = {}
        count = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i not in self.graph:
                    self.graph[i] = []
                elif isConnected[i][j] == 1 and i in self.graph:
                    self.graph[i].append(j)
        for i in self.graph:

            if i not in self.visited:
                self.dfs(i)

                count += 1
        return count


Solution().findCircleNum([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
    1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
