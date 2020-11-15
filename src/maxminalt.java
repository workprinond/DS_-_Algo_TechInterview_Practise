// IMPORT LIBRARY PACKAGES NEEDED BY YOUR PROGRAM
// SOME CLASSES WITHIN A PACKAGE MAY BE RESTRICTED
// DEFINE ANY CLASS AND METHOD NEEDED
// CLASS BEGINS, THIS CLASS IS REQUIRED
public class Solution
{
    // METHOD SIGNATURE BEGINS, THIS METHOD IS REQUIRED
    public int maxOfMinAltitudes(int columnCount, int rowCount,
                                 int[][] mat)
    {
        // WRITE YOUR CODE HERE

        int[][] dp = new int[rowCount][columnCount];
        // Init
        dp[0][0] = Integer.MAX_VALUE; // first entry is not considered
        for (int i = 1; i < rowCount; ++i) dp[i][0] = Math.min(dp[i - 1][0], mat[i][0]);
        for (int j = 1; j < columnCount; ++j) dp[0][j] = Math.min(dp[0][j - 1], mat[0][j]);
        // DP
        for (int i = 1; i < rowCount; ++i) { // row by row
            for (int j = 1; j < columnCount; ++j) {
                if (i == rowCount - 1 && j == columnCount - 1) {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]); // last entry is not considered
                } else {
                    int score1 = Math.min(dp[i][j - 1], mat[i][j]); // left
                    int score2 = Math.min(dp[i - 1][j], mat[i][j]); // up
                    dp[i][j] = Math.max(score1, score2);
                }
            }
        }
        return dp[rowCount - 1][columnCount - 1];
    }
    // METHOD SIGNATURE ENDS
}
