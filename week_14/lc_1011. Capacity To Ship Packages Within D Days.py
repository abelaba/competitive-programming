class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        maxWeight = max(weights)
        left, right = maxWeight, sum(weights)

        while left <= right:
            middle = left + (right - left) // 2

            daysCount = 1
            currentWeight = 0

            for weight in weights:
                currentWeight += weight

                if currentWeight >= middle:
                    daysCount += 1
                    currentWeight = weight

            if maxWeight == middle:
                return middle

            if daysCount > days:
                left = middle + 1
            elif daysCount <= days:
                right = middle - 1

        return right
