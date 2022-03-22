"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:

    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        answer = []

        left = 1
        right = z

        while left <= right:
            if customfunction.f(left, right) == z:
                answer.append([left, right])
                left += 1
                right -= 1
            elif customfunction.f(left, right) > z:
                right -= 1
            elif customfunction.f(left, right) < z:
                left += 1

        left = z
        right = 1

        while left >= right:
            if customfunction.f(left, right) == z:
                if [left, right] not in answer:
                    answer.append([left, right])
                left -= 1
                right += 1
            elif customfunction.f(left, right) > z:
                left -= 1
            elif customfunction.f(left, right) < z:
                right += 1

        return answer
