class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum = prices[0]

        for index in range(1, len(prices)):
            if prices[index] <= minimum:
                minimum = prices[index]
            else:
                temp = prices[index] - minimum
                max_profit = max(max_profit, temp)

        return max_profit
