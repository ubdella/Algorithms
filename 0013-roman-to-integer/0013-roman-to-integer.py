class Solution:
    def romanToInt(self, s: str) -> int:
        romToInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nextOf = {'I': {'V', 'X'}, 'X': {'L', 'C'}, 'C': {'D', 'M'}}
        
        res = 0
        i=0
        while i < len(s):
            if s[i] in nextOf and i+1 < len(s) and s[i+1] in nextOf[s[i]]:
                res+=romToInt[s[i+1]] - romToInt[s[i]]
                i+=2
            else:
                res+=romToInt[s[i]]
                i+=1
        return res
        