class Solution:
    def minimumKeypresses(self, s: str) -> int:
        char_freq = Counter(s)
        
        sorted_char = sorted(char_freq.items(), key = lambda x: x[1], reverse = True)
        
        res = 0
        
        for i, (char, freq) in enumerate(sorted_char):
            keypresses = (i//9)+1
            
            res += keypresses * freq
            
        return res