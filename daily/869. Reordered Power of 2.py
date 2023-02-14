class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))
        powersOf2 = []
        for i in range(31):
            c = Counter(str(1 << i))
            powersOf2.append(c)
        
        return any(count == powerCount for powerCount in powersOf2)
