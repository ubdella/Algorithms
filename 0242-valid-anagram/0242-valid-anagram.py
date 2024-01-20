class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        edict = {}
        for letter in s:
            if letter in edict:
                edict[letter] += 1
            else:
                edict[letter] = 1
        
        fdict = {}
        for letter in t:
            if letter in fdict:
                fdict[letter] += 1
            else:
                fdict[letter] = 1
        return edict==fdict