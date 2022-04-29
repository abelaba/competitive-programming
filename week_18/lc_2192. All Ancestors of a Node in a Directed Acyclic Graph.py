class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(set)

        ancestors = defaultdict(set)

        for fro_m, to in edges:
            graph[fro_m].add(to)

        indegrees = [0] * n

        for node in graph:
            for adj in graph[node]:
                indegrees[adj] += 1

        queue = collections.deque()

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            popped = queue.popleft()
            for child in graph[popped]:
                ancestors[child].update(ancestors[popped])
                ancestors[child].add(popped)

                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

        return [sorted(ancestors[x]) for x in range(n)]
