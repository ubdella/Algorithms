class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        oddAdded = False
        length = 0
        for key in counter:
            if counter[key]%2==0:
                length += counter[key]
            else:
                if not oddAdded:
                    length+=1
                    oddAdded = True
                length+= counter[key] - 1
        print(length)
        return length