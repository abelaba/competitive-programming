class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        numberOfBoats = 0

        while left <= right:
            if people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            numberOfBoats += 1

        return numberOfBoats
