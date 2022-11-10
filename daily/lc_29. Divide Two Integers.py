class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
                
        absDividend, absDivisor = abs(dividend), abs(divisor)
        
        quotient = 0
        num = 0
        
        for bit in bin(absDividend)[2:]:
            bit = int(bit)
            
            # Add bit to the last digit of num
            num <<= 1
            num |= bit
            
            quotient <<= 1
            
            # If num - absDivisor >= 0 add 1 to last bit of quotient
            if num >= absDivisor:
                quotient |= 1
                num -= absDivisor
        
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            
            return max(-2**31, -quotient)
        
        return min(2**31 - 1, quotient)
        
        