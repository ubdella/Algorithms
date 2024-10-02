class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(n):
            for word in wordDict:
                if i + len(word) <= n and word == s[i : i + len(word)]:
                    dp[i + len(word)] = dp[i + len(word)] or dp[i]
                    
        return dp[n]