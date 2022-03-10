import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # USING HEAP

        frequency = {}  # number , frequency
        values = []
        answer = []

        for num in nums:

            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for i in frequency:
            heapq.heappush(values, [-frequency[i], i])

        for i in range(k):
            answer.append(heapq.heappop(values)[1])
        return answer
