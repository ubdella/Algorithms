class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        def count_valid_chars(string: str, k: int) -> int:
            char_count = {}
            for char in string:
                char_count[char] = char_count.get(char, 0) + 1
            return sum(1 for count in char_count.values() if count >= k)

        def divide_and_conquer(start: int, end: int) -> int:
            if end - start < k:
                return 0

            char_count = {}
            for i in range(start, end):
                char_count[s[i]] = char_count.get(s[i], 0) + 1

            for mid in range(start, end):
                if char_count[s[mid]] < k:
                    return max(divide_and_conquer(start, mid), divide_and_conquer(mid + 1, end))

            return end - start

        return divide_and_conquer(0, len(s))    