class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        window = Counter(s2[:len(s1)])
        matchable = Counter(s1)
        i, j = 0, len(s1) - 1

        while j < len(s2):
            if window == matchable: return True
            window[s2[i]] -= 1
            
            if window[s2[i]] == 0: del window[s2[i]]
            i += 1
            j += 1
            if j < len(s2):
                window[s2[j]] = 1 + window.get(s2[j], 0)
        return False
            
            
        