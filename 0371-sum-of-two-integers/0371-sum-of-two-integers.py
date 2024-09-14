class Solution:
    def getSum(self, a, b):
        mask = 0xFFFFFFFF  # 32-bit mask
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)