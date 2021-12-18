class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        max = int(len(piles)/3) * 2
        num = 0
        while max != 0:
            num += piles[-max]
            print(-max)
            max -= 2

        return num
