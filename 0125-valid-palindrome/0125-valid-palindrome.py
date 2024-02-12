class Solution:
    def isPalindrome(self, s: str) -> bool:
        o = ''
        r = ''
        for char in s:
            if char.isalnum():
                char = char.lower()
                o = o + char
                r = char + r
        print(r)
        return r==o
            