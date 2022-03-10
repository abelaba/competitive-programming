# 5- heapSort(array)
def leftChild(index):
    return (2 * index) + 1


def rightChild(index):
    return (2*index) + 2


def parent(index):
    if index == 0:
        return index
    return (index - 1) // 2


class MaxHeap:

    def __init__(self, array=[]):
        self.array = array

    def insert(self, element):
        self.array.append(element)
        index = len(self.array) - 1
        while self.array[parent(index)] < element:
            self.array[index] = self.array[parent(index)]
            self.array[parent(index)] = element
            index = parent(index)

    def remove(self, index):
        temp = self.array[index]
        self.array[index] = self.array[-1]
        self.array[-1] = temp
        self.array.pop()
        while (leftChild(index) < len(self.array) - 1 and rightChild(index) < len(self.array) - 1) and max(self.array[leftChild(index)], self.array[rightChild(index)]) > self.array[index]:

            if self.array[leftChild(index)] > self.array[rightChild(index)]:
                temp = self.array[index]
                self.array[index] = self.array[leftChild(index)]
                self.array[leftChild(index)] = temp
                index = leftChild(index)
            elif self.array[leftChild(index)] < self.array[rightChild(index)]:
                temp = self.array[index]
                self.array[index] = self.array[rightChild(index)]
                self.array[rightChild(index)] = temp
                index = rightChild(index)
        while self.array[parent(index)] < self.array[index]:
            temp = self.array[index]
            self.array[index] = self.array[parent(index)]
            self.array[parent(index)] = temp
            index = parent(index)

    def update(self, index, element):
        self.array[index] = element
        while (leftChild(index) < len(self.array) - 1 and rightChild(index) < len(self.array) - 1) and max(self.array[leftChild(index)], self.array[rightChild(index)]) > self.array[index]:
            if self.array[leftChild(index)] > self.array[rightChild(index)]:
                self.array[index] = self.array[leftChild(index)]
                self.array[leftChild(index)] = element
                index = leftChild(index)
            elif self.array[leftChild(index)] < self.array[rightChild(index)]:
                self.array[index] = self.array[rightChild(index)]
                self.array[rightChild(index)] = element
                index = rightChild(index)
        while self.array[parent(index)] < self.array[index]:
            self.array[index] = self.array[parent(index)]
            self.array[parent(index)] = element
            index = parent(index)

    def getMin(self):
        minimum = self.array[0]
        for element in self.array:
            if element < minimum:
                minimum = element
        return minimum

    def getMax():
        return self.array[0]

    def buildHeap(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.heapify(i)

    def heapify(self, index):
        # code here
        while (leftChild(index) <= len(self.array) - 1 and rightChild(index) <= len(self.array) - 1) and max(self.array[leftChild(index)], self.array[rightChild(index)]) > self.array[index]:
            if self.array[leftChild(index)] > self.array[rightChild(index)]:
                temp = self.array[index]
                self.array[index] = self.array[leftChild(index)]
                self.array[leftChild(index)] = temp
                index = leftChild(index)
            elif self.array[leftChild(index)] < self.array[rightChild(index)]:
                temp = self.array[index]
                self.array[index] = self.array[rightChild(index)]
                self.array[rightChild(index)] = temp
                index = rightChild(index)


h = MaxHeap([1, 2, 3, 4, 5, 6, 7, 8, 9])


# h.insert(46)
# h.remove(5)
# h.update(8, 32)
# print(h.getMin())
# h.buildHeap()
# h.heapify(0)
h.buildHeap()

print(h.array)
