class Solution:
    def isAnagram( self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ls = list(s)
        lt = list(t)
        while(len(ls)!=0):
            item = ls.pop(0)
            if(item in lt):
                lt.remove(item)
            else:
                return False
        return ls==lt

                
        
        