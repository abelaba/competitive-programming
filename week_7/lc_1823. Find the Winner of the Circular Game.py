class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        array = [x for x in range(1, n+1)]
        count = 0
        while(len(array) != 1):
            if(count > len(array)-1):
                count = 0
            for i in range(k-1):
                if(count == len(array)-1):
                    count = -1
                count += 1
            array.pop(count)
        return array[0]
