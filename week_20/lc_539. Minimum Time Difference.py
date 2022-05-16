class Solution:
    def getMinute(self, time):
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        time1, time2 = self.getMinute(
            timePoints[0]), self.getMinute(timePoints[-1])

        minDiff = min(time2 - time1, time1 + 1440 - time2)
        for i in range(len(timePoints) - 1):
            if minDiff == 0:
                return 0

            time1, time2 = self.getMinute(
                timePoints[i]), self.getMinute(timePoints[i + 1])
            minDiff = min(minDiff, time2 - time1, time1 + 1440 - time2)

        return minDiff
