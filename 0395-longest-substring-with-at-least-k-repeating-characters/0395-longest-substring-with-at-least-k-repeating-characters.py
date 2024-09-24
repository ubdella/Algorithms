class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        if not s or k > len(s):
            return 0

        char_count = Counter(s)

        for char in set(s):
            if char_count[char] < k:
                return max(self.longestSubstring(substr, k) for substr in s.split(char))

        return len(s)
        