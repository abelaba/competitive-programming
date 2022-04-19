class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for n1, n2 in prerequisites:
            graph[n2].append(n1)

        degree = [0] * numCourses

        for node in graph:
            for adj in graph[node]:
                degree[adj] += 1

        queue = collections.deque()

        for i in range(numCourses):
            if not degree[i]:
                queue.append(i)

        count = 0
        while queue:
            popped = queue.popleft()
            count += 1
            for adj in graph[popped]:
                degree[adj] -= 1
                if degree[adj] == 0:
                    queue.append(adj)
                print(queue)

        return count == numCourses
