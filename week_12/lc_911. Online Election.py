from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

    def q(self, t: int) -> int:

        left = 0
        right = len(self.times) - 1

        while left <= right:

            middle = left + (right - left) // 2

            if self.times[middle-1] < t < self.times[middle]:
                left = middle-1
                break

            if t > self.times[middle]:
                left = middle
            elif t < self.times[middle]:
                right = middle
            else:
                left = middle
                break

        return self.persons[left]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
