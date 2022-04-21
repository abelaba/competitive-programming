class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        target = len(arr)
        answer = []

        while target > 0:
            index = arr.index(target)
            if index != target - 1:
                if index != 0:
                    answer.append(index + 1)
                    arr = arr[index::-1] + arr[index+1:]

                answer.append(target)
                arr = arr[target - 1::-1]
            target -= 1

        return answer
