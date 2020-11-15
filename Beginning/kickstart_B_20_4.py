





def countPaths(W:int,H:int,L:int,U:int,R:int,D:int):
    maze = [[0]* W] * H

    # maze = [[0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0]]
    # maze = [[0, 0, 0, 0, 0],
    #         [-1, -1, -1, -1, 0],
    #         [0, 0, 0, 0, 0]]
    maze = [[0, 0, 0,0,0,0],
            [0, 0,0,0,0,0],
            [-1, -1,-1,0,0,0],
            [-1, -1,-1,0,0,0]]

    # maze = [[0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0]]

    # Initializing the leftmost column
    for i in range(H):
        if (maze[i][0] == 0):
            maze[i][0] = 1

        # If we encounter a blocked cell in
        # leftmost row, there is no way of
        # visiting any cell directly below it.
        else:
            break

    # Similarly initialize the topmost row
    for i in range(1, W, 1):
        if (maze[0][i] == 0):
            maze[0][i] = 1

        # If we encounter a blocked cell in
        # bottommost row, there is no way of
        # visiting any cell directly below it.
        else:
            break

    # The only difference is that if a cell is -1,
    # simply ignore it else recursively compute
    # count value maze[i][j]
    for i in range(1, H, 1):
        for j in range(1, W, 1):

            # If blockage is found, ignore this cell
            if (maze[i][j] == -1):
                continue

            # If we can reach maze[i][j] from
            # maze[i-1][j] then increment count.
            if (maze[i - 1][j] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i - 1][j])

                # If we can reach maze[i][j] from
            # maze[i][j-1] then increment count.
            if (maze[i][j - 1] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i][j - 1])

    print(maze)



countPaths(6,4,2,2,2,2)