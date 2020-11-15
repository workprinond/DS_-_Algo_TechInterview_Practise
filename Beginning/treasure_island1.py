'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Question: Treasure Island I
You have a map that marks the location of a treasure island.
Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.
Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
The treasure island is marked as 'X' in a block of the matrix. 'X' will not be at the top-left corner.
Any block with dangerous rocks or reefs will be marked as 'D'. You must not enter dangerous blocks. You cannot leave the map area.
Other areas 'O' are safe to sail in. The top-left corner is always safe.
Output the minimum number of steps to get to the treasure.
e.g.
Input
[
['O', 'O', 'O', 'O'],
['D', 'O', 'D', 'O'],
['O', 'O', 'O', 'O'],
['X', 'D', 'D', 'O']
]
Output
Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

from collections import deque


def treasureIsland(matrix):
    '''
    # case 1 - example input
    >>> matrixA = [['O', 'O', 'O', 'O'],['D', 'O', 'D', 'O'],['O', 'O', 'O', 'O'],['X', 'D', 'D', 'O']]
    >>> treasureIsland(matrixA)
    5

    # case 2 - matrix with no treasure
    >>> matrixB = [['O', 'O', 'O', 'O'],['D', 'O', 'D', 'O'],['O', 'O', 'O', 'O'],['O', 'D', 'D', 'O']]
    >>> treasureIsland(matrixB)
    -1

    # case 3 - empty matrix 1
    >>> matrixC = []
    >>> treasureIsland(matrixC)
    -1

    # case 4 - empty matrix 2
    >>> matrixD = [[]]
    >>> treasureIsland(matrixD)
    -1
    '''
    # if matrix is empty, return -1
    if (not matrix) or (not matrix[0]):
        return -1
    # store the index of matrix and steps in queue
    queue = deque()
    queue.append([0, 0, 0])
    while queue:
        i, j, steps = queue.popleft()
        # if the treasure island is found, return the steps
        if matrix[i][j] == 'X':
            return steps
        # mark visited index
        matrix[i][j] = 'D'
        # check all the adjacent indexes
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (0 <= x < len(matrix)) and (0 <= y < len(matrix[0])) and (matrix[x][y] != 'D'):
                queue.append([x, y, steps + 1])
    # if the treasure island is not found, return -1
    return -1


if __name__ == '__main__':
    import doctest

    doctest.testmod()