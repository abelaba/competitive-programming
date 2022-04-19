class Solution:
    def dfs(self, index, graph, nonTerminal, answer):

        if not graph[index]:
            answer.add(index)
            return True

        nonTerminal.add(index)

        terminal = True

        for adj in graph[index]:
            if adj in answer:
                continue
            elif adj in nonTerminal:
                return False
            elif adj not in nonTerminal:
                terminal = terminal and self.dfs(
                    adj, graph, nonTerminal, answer)

        if terminal:
            nonTerminal.remove(index)
            answer.add(index)

        return terminal

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        answer = set()
        nonTerminal = set()

        for i in range(len(graph)):
            if i not in nonTerminal and i not in answer:
                self.dfs(i, graph, nonTerminal, answer)

        return sorted(answer)
