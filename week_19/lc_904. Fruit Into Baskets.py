class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = set()
        slow = fast = maxNumberOfFruits = 0
        fruitCount = defaultdict(int)
        numberOfTrees = len(fruits)

        while fast < numberOfTrees:
            fruit = fruits[fast]
            if fruit not in basket:
                if len(basket) < 2:
                    basket.add(fruit)
                    fruitCount[fruit] = fast
                    fast += 1
                else:
                    prevFruit = fruits[fast - 1]
                    fruit1, fruit2 = basket
                    fruitToBeRemoved = fruit1 if fruit1 != prevFruit else fruit2
                    basket.remove(fruitToBeRemoved)
                    # Get the last apperance of letter to be removed
                    slow = fruitCount[fruitToBeRemoved] + 1
            else:
                fruitCount[fruit] = fast
                fast += 1
            maxNumberOfFruits = max(maxNumberOfFruits, fast - slow)

        return maxNumberOfFruits
