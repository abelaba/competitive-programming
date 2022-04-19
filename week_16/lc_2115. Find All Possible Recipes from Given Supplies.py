class Solution:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)

        graph = {}

        for i in range(len(recipes)):
            graph[recipes[i]] = set(ingredients[i])

        degrees = [0] * len(graph)

        for i in range(len(graph)):
            for adj in graph[recipes[i]]:
                if adj in graph:
                    degrees[i] += 1

        queue = collections.deque()

        for i in range(len(degrees)):
            if degrees[i] == 0:
                queue.append(i)

        answer = set()

        while queue:
            popped = queue.popleft()
            canBeCooked = True
            for ingredient in ingredients[popped]:
                if ingredient not in supplies:
                    canBeCooked = False
                    break

            if canBeCooked:
                supplies.add(recipes[popped])
                answer.add(recipes[popped])

            for i in range(len(graph)):
                if recipes[popped] in graph[recipes[i]]:
                    degrees[i] -= 1
                    if degrees[i] == 0:
                        queue.append(i)
        return answer
