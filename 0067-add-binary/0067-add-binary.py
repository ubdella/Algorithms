class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        

        while len(a) != len(b):
            if len(a)>len(b): b = '0' + b
            if len(b)>len(a) : a = '0' + a

        
        for i in range(len(a)-1, -1, -1):
            s = carry + int(a[i]) + int(b[i])
            result = str(s%2) + result
            carry = s//2
        if carry:
            result = '1' + result
        
        return result
            
        