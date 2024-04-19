class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for char in magazine:
            if char in m:
                m[char] +=1
            else:
                m[char] = 1
        
        for char in ransomNote:
            if char in m:
                if m[char] == 1:
                    del m[char]
                else:
                    m[char] -=1
            else:
                return False
        return True