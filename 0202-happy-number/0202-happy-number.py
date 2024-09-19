class Solution:
    def isHappy(self, n: int) -> bool:
        def getDigitSquareSum(num):
            res = 0
            while num:
                res += (num % 10) ** 2
                num //= 10
            return res
                
        slow, fast = n, getDigitSquareSum(n)
        
        while slow != fast:
            fast = getDigitSquareSum(fast)
            fast = getDigitSquareSum(fast)
            slow = getDigitSquareSum(slow)
            
        return True if fast == 1 else False