public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        int[][] grid = new int[][]{{0, 1, 1, 0, 1},
                {0, 1, 0, 1, 0},
                {0, 0, 0, 0, 1},
                {0, 1, 0, 0, 0}};

        int res = getHourToTurnZombie(grid);

        System.out.println("Hours: " + res);
    }


    private static int getHourToTurnZombie(int[][] grid){
        if(grid == null || grid.length == 0 || grid[0].length == 0){
            return -1;
        }
        Queue<Point> queue = new LinkedList<>();
        int m = grid.length;
        int n = grid[0].length;
        int people = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0;j < n; j++){
                if(grid[i][j] == 1){
                    queue.offer(new Point(i, j));
                }else{
                    people++;
                }
            }
        }
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // base case
        if(people == 0){
            return 0;
        }

        for(int hour = 1; !queue.isEmpty(); hour++){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                Point p = queue.poll();
                for(int[] dir : dirs){
                    int newX = p.x + dir[0];
                    int newY = p.y + dir[1];
                    if(newX < 0 || newX >= m || newY < 0 || newY >= n
                            || grid[newX][newY] != 0){
                        continue;
                    }
                    // base case, infect all human
                    people--;
                    if(people == 0){
                        return hour;
                    }
                    // mark as zombie
                    grid[newX][newY] = 1;
                    queue.offer(new Point(newX, newY));
                }
            }
        }
        return -1;
    }

    static class Point{
        int x;
        int y;
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}