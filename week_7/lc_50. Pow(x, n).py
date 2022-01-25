class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n % 2 == 0:
                return helper(x*x, n//2)
            else:
                return x * helper(x, n-1)
        if n < 0:
            n = -1 * n
            return 1/(helper(x, n))

        return helper(x, n)
