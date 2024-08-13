class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l<=r:
            m = (l+r)//2
            if isBadVersion(m):
                res =  m
                r = m-1
            else:
                l = m+1
        return res