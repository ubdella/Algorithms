class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCounter = Counter(magazine)
        noteCounter = Counter(ransomNote)
        
        for key in noteCounter.keys():
            if key not in magCounter or noteCounter[key]>magCounter[key]: return False
            
        return True