class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache
        def dp(i):
            if i == n:
                return True
            for word in wordDict:
                if i + len(word) <= n and word == s[i: i + len(word)]:
                    if dp(i + len(word)):
                        return True
            return False
        return dp(0)