class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        changed.sort()
        dictionary = defaultdict(lambda: 0)
        array = []

        # adding array count in dictionary
        for i in changed:
            dictionary[i] += 1

        for i in changed:
            if(i*2 in dictionary and dictionary[i] != 0):
                dictionary[i] -= 1
                dictionary[i*2] -= 1
                array.append(i)
            elif(i*2 not in dictionary and dictionary[i] != 0):
                return []

        # checking if there is any element in dictionary that has count > 0
        for i in dictionary:
            if dictionary[i] != 0:
                return
        return array
