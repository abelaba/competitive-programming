class Solution:
    
    def buildArray(self, graph, visited, answer, node):
        
        visited.add(node)
        answer.append(node)
        
        for adj in graph[node]:
            if adj not in visited:
                self.buildArray(graph, visited, answer, adj)
        
    
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        start = 0
        
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break
        
        answer = []
        
        self.buildArray(graph, set(), answer, start)
        
        return answer
        
