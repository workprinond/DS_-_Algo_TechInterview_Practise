public class Main {
    /*
     Approach:
     We use a BFS(breadth-first search) to find the target.
     We also use 2D-array to record the position we have visited.
     For a position, we put its neighbor in the queue if its neighbor is not visited or its value is not '0'.
     We continue the BFS search until we reach the target. The length of the path is the minimal path to reach the target.
     Time complexity: We at most check each position in the quque. So the time complexity is O(M*N)
    Space complexity: We use a 2 dimension array to record the visited position. So the space complexity is O(M*N)
 */
    public static void main(String args[])
    {
        char[][] island = new char[][]{
                {'O', 'O', 'O', 'O'},
                {'D', 'O', 'D', 'O'},
                {'O', 'O', 'O', 'O'},
                {'X', 'D', 'D', 'O'}
        };
        int result = treasureIsland(island);
        System.out.println(String.format("%s ", result));
    }


    public static int treasureIsland(char[][] island){
        if(island == null || island.length == 0){
            return 0;
        }

        Queue<Coordinate> queue = new LinkedList<>();
        boolean[][] visited = new boolean[island.length][island[0].length];
        queue.offer(new Coordinate(0, 0));
        visited[0][0] = true;

        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int steps = 0;

        while (!queue.isEmpty()) {

            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Coordinate coordinate = queue.poll();
                int x = coordinate.x;
                int y = coordinate.y;
                if (island[x][y] == 'X') return steps;

                for (int[] dir : dirs) {
                    int newX = x + dir[0];
                    int newY = y + dir[1];

                    if (newX >= 0 && newX < island.length && newY >= 0 && newY <                        island[0].length &&
                            island[newX][newY] != 'D' && !visited[newX][newY]) {
                        queue.add(new Coordinate(newX, newY));
                        visited[newX][newY] = true;
                    }
                }
            }
            steps++;
        }
        return 0;
    }


    static class Coordinate{
        int x;
        int y;

        public Coordinate(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}