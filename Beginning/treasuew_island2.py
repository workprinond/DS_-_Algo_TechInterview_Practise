'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Question: Treasure Island II
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure island.
Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from one of the starting point(marked as 'S') of the map and can move one block up, down, left or right at a time.
The treasure island is marked as 'X' in a block of the matrix.
Any block with dangerous rocks or reefs will be marked as 'D'. You must not enter dangerous blocks. You cannot leave the map area.
Other areas 'O' are safe to sail in.
Output the minimum number of steps to get to any of the treasure.
e.g.
Input
[
['S', 'O', 'O', 'S', 'S'],
['D', 'O', 'D', 'O', 'D'],
['O', 'O', 'O', 'O', 'X'],
['X', 'D', 'D', 'O', 'O'],
['X', 'D', 'D', 'D', 'O']
]
Output
3
Explanation
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

from collections import deque


def treasureIsland2(matrix):
    '''
    # case 1 - example input
    >>> matrixA = [['S', 'O', 'O', 'S', 'S'],['D', 'O', 'D', 'O', 'D'],['O', 'O', 'O', 'O', 'X'],['X', 'D', 'D', 'O', 'O'],['X', 'D', 'D', 'D', 'O']]
    >>> treasureIsland2(matrixA)
    3

    # case 2 - modified example input
    >>> matrixB = [['S', 'O', 'O', 'S', 'S'],['D', 'O', 'D', 'O', 'D'],['O', 'O', 'O', 'O', 'O'],['X', 'D', 'D', 'O', 'O'],['X', 'D', 'D', 'D', 'O']]
    >>> treasureIsland2(matrixB)
    5

    # case 3 - modified example input 2
    >>> matrixC = [['S', 'O', 'O', 'S', 'S'],['D', 'O', 'D', 'O', 'D'],['O', 'O', 'O', 'O', 'O'],['O', 'D', 'D', 'O', 'O'],['X', 'D', 'D', 'D', 'O']]
    >>> treasureIsland2(matrixC)
    6

    # case 4 - matrix with no treasure
    >>> matrixD = [['S', 'O', 'O', 'S', 'S'],['D', 'O', 'D', 'O', 'D'],['O', 'O', 'O', 'O', 'O'],['O', 'D', 'D', 'O', 'O'],['O', 'D', 'D', 'D', 'O']]
    >>> treasureIsland2(matrixD)
    -1

    # case 5 - empty matrix 1
    >>> matrixE = []
    >>> treasureIsland2(matrixE)
    -1

    # case 6 - empty matrix 2
    >>> matrixF = [[]]
    >>> treasureIsland2(matrixF)
    -1

    # case 7 - customized matrix (2 starting points, 1 starting point has no way to get 'X')
    >>> matrixG = [['S', 'D', 'O', 'O', 'O'], ['D', 'O', 'O', 'D', 'O'], ['D', 'O', 'D', 'D', 'O'], ['O', 'O', 'X', 'D', 'O'], ['O', 'D', 'D', 'D', 'S']]
    >>> treasureIsland2(matrixG)
    11

    # case 8 - customized matrix 2 (no starting point)
    >>> matrixH = [['D', 'O', 'O', 'O', 'O'], ['D', 'O', 'O', 'D', 'O'], ['D', 'O', 'D', 'D', 'O'], ['O', 'O', 'X', 'D', 'O'], ['O', 'D', 'D', 'D', 'O']]
    >>> treasureIsland2(matrixH)
    -1

    # case 9 - customized matrix 3 (multiple treasure)
    >>> matrixI = [['X', 'O', 'O', 'O', 'D', 'D'], ['D', 'D', 'D', 'O', 'D', 'D'], ['X', 'O', 'O', 'O', 'D', 'S'], ['D', 'D', 'O', 'D', 'D', 'D'], ['S', 'O', 'O', 'O', 'D', 'X']]
    >>> treasureIsland2(matrixI)
    6
    '''
    # if matrix is empty, return -1
    if (not matrix) or (not matrix[0]):
        return -1
    # set minSteps as infinity
    minSteps = float('inf')
    # if 'S' is found in matrix, get steps to every 'X'
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                curSteps = bfs(matrix, i, j)
                # compare each steps and store smaller steps
                minSteps = min(minSteps, curSteps)
    # if minSteps is infinity, it did not find a way to get 'X', so return -1
    return -1 if minSteps == float('inf') else minSteps


def bfs(matrix, i, j):
    # create set that stores visited indexes
    visited = set()
    # store the index of matrix and steps in queue
    queue = deque()
    queue.append([i, j, 0])
    while queue:
        i, j, steps = queue.popleft()
        # mark visited index
        visited.add((i, j))
        # if the treasure island is found, return the steps
        # I can just return it without finding another 'X'
        # because this is the shortest path
        if matrix[i][j] == 'X':
            return steps
            # check all the adjacent indexes
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (0 <= x < len(matrix)) and (0 <= y < len(matrix[0])) and (matrix[x][y] != 'D') and (
                    (x, y) not in visited):
                queue.append([x, y, steps + 1])
    # if the treasure island is not found, return infinity
    return float('inf')


if __name__ == '__main__':
    import doctest

    doctest.testmod()