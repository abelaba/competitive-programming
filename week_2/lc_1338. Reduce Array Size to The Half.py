class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        countArray = [0]
        num = arr[0]
        for i in arr:
            if(i != num):
                num = i
                countArray.append(0)
            countArray[-1] += 1
        countArray.sort(reverse=True)
        sum = 0
        count = 0
        for i in countArray:
            sum += i
            count += 1
            if(sum >= len(arr) / 2):
                break
        return count
