class Solution:
       
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        ancestors = defaultdict(set)
        
        for parent, child in prerequisites:
            graph[parent].add(child)
        
        
        indegrees = [0] * numCourses
        
        for node in graph:
            for adj in graph[node]:
                indegrees[adj] += 1
        
        
        queue = collections.deque()
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
                ancestors[i] = set()
                
        
        while queue:
            popped = queue.popleft()
            
            for child in graph[popped]:
                ancestors[child].update(ancestors[popped])
                ancestors[child].add(popped)
                
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

        
        answer = []
        for parent, child in queries:
            if parent in ancestors[child]:
                answer.append(True)
            else:
                answer.append(False)
        return answer
            
        
            
        
        
        
        