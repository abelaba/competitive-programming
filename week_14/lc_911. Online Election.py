from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.times = times

        self.leaders = []

        counter = {}

        for i in range(len(persons)):
            person = persons[i]

            if person in counter:
                counter[person] += 1
            else:
                counter[person] = 1

            if not self.leaders:
                self.leaders.append(person)
            else:
                prevLeader = self.leaders[-1]
                if counter[person] >= counter[prevLeader]:
                    self.leaders.append(person)
                else:
                    self.leaders.append(prevLeader)

    def q(self, t: int) -> int:

        left = 0
        right = len(self.times) - 1

        while left <= right:

            middle = left + (right - left) // 2

            middlElement = self.times[middle]

            if self.times[middle - 1] < t < middlElement:
                left = middle - 1
                break

            if t > middlElement:
                left = middle + 1
            elif t < middlElement:
                right = middle - 1
            else:
                left = middle
                break

        if left == len(self.leaders):
            return self.leaders[-1]
        return self.leaders[left]

# ,"q","q","q","q","q","q","q","q","q"
# ,[49],[59],[68],[42],[37],[99],[26],[78],[43]
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
