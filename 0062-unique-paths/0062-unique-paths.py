class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =  [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if j < n - 1:
                    dp[i][j + 1] += dp[i][j]
                if i < m - 1:
                    dp[i + 1][j] += dp[i][j]                
                
        return dp[i][j]
        