class Solution:
    def find(self, parent: array, x: int) -> int:
        if parent[x] == x:
            return x
        return self.find(parent, parent[x])

    def union(self, parent: array, x: int, y: int, rank: dict) -> (bool, int):
        xRoot = self.find(parent, x)
        yRoot = self.find(parent, y)

        if xRoot == yRoot:
            return False, 0

        if rank[xRoot] >= rank[yRoot]:
            parent[yRoot] = xRoot
            rank[xRoot] += rank[yRoot]
            totalNodes = rank[xRoot]
            rank[yRoot] = 0
        else:
            parent[xRoot] = yRoot
            rank[yRoot] += rank[xRoot]
            rank[xRoot] = 0
            totalNodes = rank[yRoot]

        return True, totalNodes

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        length = len(points)
        parents = [x for x in range(length)]
        rank = defaultdict(lambda: 1)

        graph = []
        for i in range(length):
            for j in range(i + 1, length):
                distance = abs(points[i][0] - points[j][0]) + \
                    abs(points[i][1] - points[j][1])
                graph.append((distance, i, j))

        graph.sort()

        answer = 0
        for weight, start, end in graph:
            canBeMerged, nodesUsed = self.union(parents, start, end, rank)
            if canBeMerged:
                answer += weight
                if nodesUsed == length:
                    return answer
        return answer
