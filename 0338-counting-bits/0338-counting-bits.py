class Solution:
    def countBits(self, n: int) -> List[int]:
        def getOnes(bits):
            ones = 0
            while bits:
                if bits % 2 != 0:
                    ones += bits & 1
                bits = bits >> 1
            return ones
        res = []
        for digit in range(n + 1):
            res.append(getOnes(digit))
        return res