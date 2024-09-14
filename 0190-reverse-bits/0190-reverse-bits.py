class Solution:
    def reverseBits(self, n):
        res = 0

        for i in range(32):

            res = res << 1
            bit = n%2
            res += bit
            n = n >> 1

        return res
        