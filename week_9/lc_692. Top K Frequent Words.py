class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}  # number , frequency
        values = []
        answer = []

        for word in words:

            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

        for i in frequency:
            heapq.heappush(values, [-frequency[i], i])

        for i in range(k):
            answer.append(heapq.heappop(values)[1])
        return answer
