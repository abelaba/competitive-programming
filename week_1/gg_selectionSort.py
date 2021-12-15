# User function Template for python3

class Solution:
    def select(self, arr, i):
        return arr[i]

    def selectionSort(self, arr, n):
        min = 0
        for i in range(0, len(arr)):
            min = i
            for j in range(i, len(arr)):
                if(arr[min] >= arr[j]):
                    min = j
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends
