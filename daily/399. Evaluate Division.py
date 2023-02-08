class Solution:
    
    
    def dfs(self, formulas, visited, node1, node2):
        
        if node1 == node2: return 1
        
        visited.add(node1)
        
        for value, node in formulas[node1]:
            if node not in visited:
                ans = value * self.dfs(formulas, visited, node, node2)
                if ans: return ans
        
        return 0
            
            
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        N = len(equations)
        
        formulas = defaultdict(list)
        
        
        for i in range(N):
            x, y = equations[i]
            value = values[i]
            formulas[x].append((value, y))
            formulas[y].append((1 / value, x))
            
        
        answer = []
        
        for query in queries:
            x, y = query
            if x not in formulas or y not in formulas:
                answer.append(-1)
                continue
            find = self.dfs(formulas,set() , x, y)
            answer.append(find if find != 0 else -1)
               
        return answer
            
