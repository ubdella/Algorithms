class Solution:
    def hammingWeight(self, n: int) -> int:
        binary  = bin(n)
        print(binary)
        cnt = 0
        for digit in binary:
            if digit == '1':
                cnt += 1
        return cnt