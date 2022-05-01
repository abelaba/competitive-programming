class Solution:
    def dfs(self, graph, node, minDistances, n):
        if node == n:
            return 1

        if node in self.memo:
            return self.memo[node]

        paths = 0
        for child, size in graph[node]:
            if minDistances[node - 1] > minDistances[child - 1]:
                paths += self.dfs(graph, child, minDistances, n)

        self.memo[node] = paths
        return paths

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for start, end, weight in edges:
            graph[start].append((end, weight))
            graph[end].append((start, weight))

        heap = [(0, n)]
        minDistances = {}
        minDistances[n - 1] = 0
        seen = set()
        while heap:
            weight, index = heappop(heap)
            if index not in seen:
                seen.add(index)
                minDistances[index - 1] = weight
                for child, size in graph[index]:
                    if child not in seen:
                        heappush(heap, (weight + size, child))

        self.memo = {}
        return self.dfs(graph, 1, minDistances, n) % (10**9 + 7)
