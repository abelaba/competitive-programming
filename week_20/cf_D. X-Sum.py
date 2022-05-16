import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def check(row, col, n, m):
    if 0 <= row < n and 0 <= col < m:
        return True


def traverse(grid, row, col, direction, diags):
    for x, y in direction:
        newRow, newCol = x + row, y+col
        if check(newRow, newCol, len(grid), len(grid[0])):
            diags.append(grid[newRow][newCol])
            traverse(grid, newRow, newCol, [[x, y]], diags)


t = inp()
answer = []
for i in range(t):
    n, m = inlt()
    grid = []
    for i in range(n):
        grid.append(inlt())
    direction = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    maxSum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            diags = [grid[i][j]]
            traverse(grid, i, j, direction, diags)
            maxSum = max(maxSum, sum(diags))
    answer.append(maxSum)

for ans in answer:
    print(ans)
