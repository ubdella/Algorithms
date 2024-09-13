class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # Base case: empty string is valid
        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n - 1 and (s[i] == '(' or s[i] == '*') and (s[i+1] == ')' or s[i+1] == '*'):
                dp[i][i+1] = True
        
        # Fill the dp table
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if (s[i] == '(' or s[i] == '*') and (s[j] == ')' or s[j] == '*'):
                    dp[i][j] = dp[i+1][j-1]
                
                for k in range(i, j):
                    dp[i][j] |= dp[i][k] and dp[k+1][j]
        
        return dp[0][n-1]