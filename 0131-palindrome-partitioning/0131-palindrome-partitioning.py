class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur, res = [], []        
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def dfs(i):
            if i >= len(s):
                res.append(cur.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    cur.append(s[i:j+1])
                    dfs(j + 1)
                    cur.pop()
        dfs(0)
        return res
    
    
