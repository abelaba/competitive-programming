class Solution:
    def calculateSqrt(self, i):
        ans = math.sqrt(i[0]**2 + i[1]**2)
        return ans

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: self.calculateSqrt(x))
        return points[0:k]
