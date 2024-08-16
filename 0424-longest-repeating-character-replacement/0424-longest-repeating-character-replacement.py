class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = longest = 0
        counts = {}
        for j in range(len(s)):
            counts[s[j]] = 1 + counts.get(s[j], 0)
            
            if j - i + 1 - max(counts.values()) > k:
                counts[s[i]] -= 1
                i += 1
                continue
            
            longest = max(longest, j - i + 1)
        
        
                
        return longest
                
            
                