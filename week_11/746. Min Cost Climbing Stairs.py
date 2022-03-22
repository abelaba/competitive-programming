class Solution:
    def findSteps(self, position, cost, memo):
        if position in memo:
            return memo[position]

        if position >= len(cost):
            return 0

        if position == len(cost) - 1:
            return cost[position]

        walk = self.findSteps(position + 1, cost, memo)
        jump = self.findSteps(position + 2, cost, memo)

        memo[position] = cost[position] + min(walk, jump)

        return memo[position]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        minimum = min(self.findSteps(0, cost, memo),
                      self.findSteps(1, cost, memo))
        return minimum
