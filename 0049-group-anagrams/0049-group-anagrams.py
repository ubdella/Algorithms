class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for word in strs:
            key = "".join(sorted(word))
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]

        return res.values()
            



