class Solution:
    def reverse(self, x):
        # Determine the sign of the input
        sign = 1 if x >= 0 else -1
        x = abs(x)

        reversed_num = 0
        while x != 0:
            # Check for potential overflow before adding the next digit
            if reversed_num > (2**31 - 1) // 10:
                return 0

            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return sign * reversed_num