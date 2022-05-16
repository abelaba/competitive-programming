class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        leadingZeros = 32 - len(binary)

        binary = '0' * leadingZeros + binary

        return int(binary[::-1], 2)
