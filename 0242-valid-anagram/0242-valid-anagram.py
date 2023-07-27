class Solution:
    def isAnagram( self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        smap = {}
        tmap = {}
        
        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i],0) + 1
            tmap[t[i]] = tmap.get(t[i],0) + 1

        return smap==tmap



                
        
        