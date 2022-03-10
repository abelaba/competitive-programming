import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        maxHeap = []

        for row in range(len(matrix)):
            for col in range(len(matrix)):
                value = -matrix[row][col]
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, value)
                else:
                    if value > maxHeap[0]:
                        heapq.heappushpop(maxHeap, value)

        return -maxHeap[0]
