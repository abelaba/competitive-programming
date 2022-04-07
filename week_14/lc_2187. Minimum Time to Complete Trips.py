class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips
        answer = 1

        while left <= right:
            mid = left + (right - left) // 2

            trip = 0
            for t in time:
                trip += mid // t

            if trip < totalTrips:
                left = mid + 1
            elif trip >= totalTrips:
                right = mid - 1

        return left
