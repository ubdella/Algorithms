class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]
        
        return [group for group in anagram_groups.values() if len(group) > 0]





