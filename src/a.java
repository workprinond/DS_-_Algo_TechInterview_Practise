else
        {
        // Assume there is at least one element

        int[] dp = new int[columnCount];
        // Init
        dp[0] = Integer.MAX_VALUE; // first entry is not considered
        for (int j = 1; j < columnCount; ++j) dp[j] = Math.min(dp[j - 1], mat[0][j]);
        // DP (for each row)
        for (int i = 1; i < rowCount; ++i) {
        // update the first element in each row
        dp[0] = Math.min(dp[0], mat[i][0]);
        for (int j = 1; j < columnCount; ++j) {
        if (i == rowCount - 1 && j == columnCount - 1) {
        dp[j] = Math.max(dp[j - 1], dp[j]); // last entry is not considered
        } else {
        int score1 = Math.min(dp[j - 1], mat[i][j]); // left  dp[i][j-1]
        int score2 = Math.min(dp[j], mat[i][j]);     // up    dp[i-1][j]
        dp[j] = Math.max(score1, score2);
        }
        }
        }
        return dp[columnCount - 1];
        }