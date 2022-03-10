
def inlt():
    return(list(map(int, input().split())))


class Solution:

    def check(self, row, col, m, n):
        if 0 <= row < m and 0 <= col < n:
            return True

    def dfs(self, row, col, grid, visited, DIR, binary_indicies):
        openings = []
        count = 1

        for index in binary_indicies:
            if grid[row][col] & index == 0:
                openings.append(0)
            else:
                openings.append(1)
        visited.append([row, col])

        for i in range(len(openings)):
            if openings[i] == 0:
                newRow, newCol = row + DIR[i][0], col + DIR[i][1]
                if self.check(newRow, newCol, len(grid), len(grid[0])) and [newRow, newCol] not in visited:
                    count += self.dfs(newRow, newCol, grid,
                                      visited, DIR, binary_indicies)
        return count

    def numberOfRoomsFinder(self, array):
        DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = []
        binary_indicies = [8, 4, 2, 1]
        rooms = []
        for row in range(len(array)):
            for col in range(len(array[0])):
                if [row, col] not in visited:
                    rooms.append(self.dfs(row, col, array,
                                 visited, DIR, binary_indicies))
        rooms.sort(reverse=True)

        for room in rooms:
            print(room, end=" ")


def main():
    matrixDimention = inlt()
    array = []
    for i in range(matrixDimention[0]):
        array.append(inlt())
    Solution().numberOfRoomsFinder(array)


main()
