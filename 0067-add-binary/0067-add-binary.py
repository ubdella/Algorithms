class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        
        if len_a > len_b:
            for i in range(len_a - len_b):
                b = '0' + b
        else:
            for i in range(len_b - len_a):
                a = '0' + a
        if a == b == '0':
            return '0'
        carry = 0
        result = ''
        for i in range(len(a)-1, -1, -1):
            s = int(a[i]) + int(b[i]) + carry
            if i == 0:
                if s == 0:
                    return result
                elif s == 1:
                    return '1' + result
                elif s == 2:
                    return '10' + result
                elif s == 3:
                    return '11' + result
                
                    
            if s == 2:
                carry = 1
                result = '0' + result
            elif s == 3:
                carry = 1
                result = '1' + result
            elif s == 1:
                carry = 0
                result = '1' + result
            else:
                carry = 0
                result = '0' + result
            
        