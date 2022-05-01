class Solution:

    def dfs(self, graph, node, shortestDistToLastNode, su_m, n):
        if node in self.memo:
            return self.memo[node]

        if node == n - 1:
            return 1

        minPaths = 0
        for weight, index in graph[node]:
            totalWeight = su_m + weight
            if totalWeight + shortestDistToLastNode[index] == shortestDistToLastNode[0]:

                minPaths += self.dfs(graph, index,
                                     shortestDistToLastNode, totalWeight, n)

        self.memo[node] = minPaths
        return self.memo[node]

    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(list)

        # making the adjecency list graph
        for start, end, weight in roads:
            graph[start].append((weight, end))
            graph[end].append((weight, start))

        # dikstra algo
        shortestDistToLastNode = {}
        heap = [[0, n - 1]]
        seen = set()

        while heap:
            weight, index = heapq.heappop(heap)
            if index not in seen:
                seen.add(index)
                shortestDistToLastNode[index] = weight
                for cost, adj in graph[index]:
                    if adj not in seen:
                        heapq.heappush(heap, (cost + weight, adj))

        self.memo = {}
        return self.dfs(graph, 0, shortestDistToLastNode, 0, n) % (10**9 + 7)
