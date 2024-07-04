class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqs = Counter(s)
        res = 0
        odd = False
        for freq in freqs.values():
            if freq%2==0:
                res+=freq
            else:
                odd = True
                res+=freq-1
                
        res+=odd
        return res