class Solution:
    def numDecodings(self,s):
        if int(s[0]) == 0:
            return 0
        @cache
        def dp(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == '0':
                return 0
            numWays = dp(i + 1)
            if int(s[i : i + 2]) <= 26:
                numWays += dp(i + 2)
            return numWays 
        return dp(0)