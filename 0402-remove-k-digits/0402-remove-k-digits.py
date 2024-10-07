class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If we still need to remove digits, remove from the end
        stack = stack[:-k] if k > 0 else stack
        
        # Convert stack to string and remove leading zeros
        result = "".join(stack).lstrip("0")
        
        return result if result else "0"