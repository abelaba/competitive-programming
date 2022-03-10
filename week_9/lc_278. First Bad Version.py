# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            middle = left + (right - left) // 2
            if not isBadVersion(middle):
                left = middle + 1
            elif isBadVersion(middle):
                right = middle - 1

        return left
