class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        graph = defaultdict(list)
        
        for bus in range(len(routes)):
            route = routes[bus]                        
            
            for r in route:
                graph[r].append(bus)
                
        
        
        queue = deque()
        queue.append((source, 0)) # node, depth
        
        visitedRoute = {source}
        visitedBus = set()
        
        level = 0
        
        while queue:
            
            node, depth = queue.popleft()
            
            if node == target:
                return depth
            
            for bus in graph[node]:
                if bus in visitedBus:
                    continue
                
                visitedBus.add(bus)
                
                for route in routes[bus]:
                    if route in visitedRoute:
                        continue
                    
                    visitedRoute.add(route)
                    queue.append((route, depth+1))
                    

        return -1
            
        
        
        
        
