# User function Template for python3
import sys
import io
import atexit


def leftChild(index):
    return (2 * index) + 1


def rightChild(index):
    return (2*index) + 2


class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, index):
        # code here
        maximum = index
        while (leftChild(index) <= n-1):

            if arr[leftChild(index)] > arr[maximum]:
                # arr[index], arr[leftChild(index)] = arr[leftChild(index)], arr[index]
                maximum = leftChild(index)

            if rightChild(index) <= n - 1 and arr[maximum] < arr[rightChild(index)]:
                # arr[index], arr[rightChild(index)] = arr[rightChild(index)],arr[index]
                maximum = rightChild(index)
            if maximum != index:
                arr[maximum], arr[index] = arr[index], arr[maximum]
                index = maximum
            else:
                break

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # code here
        for i in range(n - 1, -1, -1):
            self.heapify(arr, n, i)
            # Function to sort an array using Heap Sort.

    def HeapSort(self, arr, n):
        # code here
        self.buildHeap(arr, n)

        for i in range(n):
            arr[0], arr[n-i-1] = arr[n-i-1], arr[0]
            self.heapify(arr, n-i-1, 0)
            # print(arr)


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr, n)
        print(*arr)

# } Driver Code Ends
