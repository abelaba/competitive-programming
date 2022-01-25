class Solution:
    def reverse(self, val):
        return val[::-1]

    def invert(self, val):
        value = ""
        for i in val:
            if i == "1":
                value += "0"
            else:
                value += "1"
        return value

    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return "0"
            else:
                data = helper(n - 1)
                return data + "1" + self.reverse(self.invert(data))
        rec = helper(n)
        return rec[k - 1]
