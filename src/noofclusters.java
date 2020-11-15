public class noofclusters {
    public int numIslands(char[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0){
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;

        int res = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1'){
                    res++;
                    helper(i, j, m, n, grid);
                }
            }
        }
        return res;
    }

    private void helper(int i, int j, int m, int n, char[][] grid){
        if(i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0'){
            return;
        }
        grid[i][j] = '0';
        helper(i - 1, j, m, n, grid);
        helper(i + 1, j, m, n, grid);
        helper(i, j - 1, m, n, grid);
        helper(i, j + 1, m, n, grid);
    }
}
