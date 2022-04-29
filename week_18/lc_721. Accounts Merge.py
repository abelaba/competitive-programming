class Solution:
    def find(self, parent, x):
        if parent[x] == x:
            return x
        return self.find(parent, parent[x])

    def union(self, parent, x, y, rank):
        xRoot = self.find(parent, x)
        yRoot = self.find(parent, y)

        if rank[xRoot] >= rank[yRoot]:
            parent[xRoot] = yRoot
            rank[xRoot] += rank[yRoot]
            rank[yRoot] = 0
        else:
            parent[yRoot] = xRoot
            rank[yRoot] += rank[xRoot]
            rank[xRoot] = 0

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rank = defaultdict(lambda: 1)

        parent = {}

        for account in accounts:
            for i in range(1, len(account)):
                parent[account[i]] = account[i]

        for account in accounts:
            for i in range(1, len(account) - 1):
                self.union(parent, account[i], account[i+1], rank)

        mergedAccounts = defaultdict(set)

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                acc = account[i]
                mergedAccounts[self.find(parent, acc), name].add(acc)

        answer = []
        for account in mergedAccounts:
            sortedAccounts = sorted(mergedAccounts[account])
            value = [account[1]] + sortedAccounts
            answer.append(value)

        return answer
