class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):

            back = i - 1
            front = i + 1
            areBothZero = True

            if back >= 0 and flowerbed[back] == 1:
                areBothZero = areBothZero and False

            if front < len(flowerbed) and flowerbed[front] == 1:
                areBothZero = areBothZero and False

            if areBothZero and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

            if n == 0:
                return True
