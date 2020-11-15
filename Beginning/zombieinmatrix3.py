def solution(grid):
    count, queue = 0, []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                queue.append((i, j, 0))

    while queue:
        x, y, count = queue.pop(0)
        perimeter = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        for i, j in perimeter:
            if i > -1 and i < len(grid) and j > -1 and j < len(grid[0]) and grid[i][j] == 0:
                grid[i][j] = 1
                queue.append((i, j, count + 1))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 1:
                return -1

    return count


print(solution([[0, 1, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0]]))