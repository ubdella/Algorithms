class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #initialize frequency for each character with 0
        #initialize a left, intialize a result
        #for traversing right pointer until the end of the string
        #	update the counts
        #	go through the counts to find the highest frequency element
        #	if window length - highest frequency > k
        #		left += 1
        #	take the max of result and windowlength

        #“AAAABBCCC” k = 2
        #freq = {A: 3, B:2, C:2}
        freq = [0] * 26
        left = result = 0
        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] += 1
            if right - left + 1 - max(freq) > k:

                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

            
                