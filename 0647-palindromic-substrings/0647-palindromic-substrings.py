class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def subs(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
                
        for i in range(len(s)):
            l = r = i
            subs(l, r)
            subs(l, r + 1)
            
        return res
                
        
                
                