class Solution:
    def countBits(self, n: int) -> List[int]:
        def getOnes(bits):
            ones = 0
            while bits:
                ones += 1
                bits = bits & (bits - 1)
            return ones
        res = []
        for digit in range(n + 1):
            res.append(getOnes(digit))
        return res