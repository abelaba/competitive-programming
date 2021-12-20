class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        frequencyArray = [[nums[0], 0]]
        for i in nums:
            if i == frequencyArray[-1][0]:
                frequencyArray[-1][1] += 1
            else:
                frequencyArray.append([i, 1])
        print(frequencyArray)
        frequencyArray.sort(key=lambda x: x[1], reverse=True)
        array = [i[0] for i in frequencyArray]
        return array[:k]
