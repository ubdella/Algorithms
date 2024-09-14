class Solution:
    def reverseBits(self, n):
        # Convert to binary string, remove '0b' prefix, zero-pad to 32 bits
        binary_str = format(n, '032b')
        # Reverse the string
        reversed_str = binary_str[::-1]
        # Convert back to integer
        return int(reversed_str, 2)
        