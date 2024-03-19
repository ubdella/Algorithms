class Solution:
    def calculate(self, s):    
        def update(op, n):
            if op == '+': stack.append(n)
            if op == '-': stack.append(-n)
            if op == '/': stack.append(stack.pop()/n)
            if op == '*': stack.append(stack.pop()*n)
                
        stack, i, num, sign = [], 0, 0, '+'
        
        while i<len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
                
            elif s[i] in "+-*/":
                update(sign, num)
                sign = s[i]
                num = 0
                
            elif s[i] == '(':
                num, j  = self.calculate(s[i+1:])
                i+=j
            elif s[i] == ')':
                update(sign, num)
                return sum(stack), i+1
                
            i+=1
            
        update(sign, num)
        return sum(stack)