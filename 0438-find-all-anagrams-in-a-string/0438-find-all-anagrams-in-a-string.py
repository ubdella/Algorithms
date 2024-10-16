class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        targetFreq = [0] * 26
        for c in p:
            targetFreq[ord(c) - ord('a')] += 1
        curFreq = [0] * 26
        result = []
        left = 0
        for right in range(len(s)):
            curFreq[ord(s[right]) - ord('a')] += 1
            if right >= len(p):
                curFreq[ord(s[left]) - ord('a')] -= 1
                left += 1
            if curFreq == targetFreq:
                result.append(left)
        return result       