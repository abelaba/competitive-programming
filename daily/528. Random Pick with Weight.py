class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        prefixSum = 0
        
        for i in range(len(w)):
            prefixSum += w[i]
            self.weights.append((prefixSum, i))
        
        self.totalWeight = prefixSum
        
            
    def binarySearch(self, target):
        left = 0
        right = len(self.weights) - 1
        
        while left <= right:
            mid = left + (right-left) // 2
            
            if target <= self.weights[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        

    def pickIndex(self) -> int:
        
        randomWeight =  random.randint(1, self.totalWeight)
        
        findPosition = self.binarySearch(randomWeight)
        
        return self.weights[findPosition][1]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
