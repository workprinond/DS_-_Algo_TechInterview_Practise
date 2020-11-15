public class Main {

    public static int minDist(char[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0){
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        Queue<Point> queue = new LinkedList<>();
        collectStartPoint(queue, grid);
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int steps = 0;
        while(!queue.isEmpty()){
            steps++;
            int size = queue.size();
            for(int i = 0; i < size; i++){
                Point p = queue.poll();
                // marka as visited
                grid[p.x][p.y] = 'D';

                for(int[] dir : dirs){
                    int newX = p.x + dir[0];
                    int newY = p.y + dir[1];
                    if(newX < 0 || newX >= m || newY < 0 || newY >= n
                            || grid[newX][newY] == 'D'){
                        continue;
                    }
                    if(grid[newX][newY] == 'X'){
                        return steps;
                    }
                    queue.offer(new Point(newX, newY));
                }
            }
        }
        return -1;
    }

    private static void collectStartPoint(Queue<Point> queue, char[][] grid){
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 'S'){
                    queue.offer(new Point(i, j));
                }
            }
        }
    }

    public static void main(String[] args) {
        char[][] grid = {
                {'S', 'O', 'O', 'S', 'S'},
                {'D', 'O', 'D', 'O', 'D'},
                {'O', 'O', 'O', 'O', 'X'},
                {'X', 'D', 'D', 'O', 'O'},
                {'X', 'D', 'D', 'D', 'O'}};

        System.out.println("Steps" + minDist(grid));
    }
}
class Point{
    int x;
    int y;
    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}