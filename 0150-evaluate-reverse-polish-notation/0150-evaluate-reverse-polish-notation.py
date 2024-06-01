class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def evaluate(x,y,o):
            if o == '+':
                return x+y
            elif o == '-':
                return x-y
            elif o == '*':
                return x*y
            else:
                return int(x/y)
        for symbol in tokens:
            if symbol in "+-*/":
                y = stack.pop()
                x = stack.pop()
                stack.append(evaluate(x,y,symbol))       

            else:
                stack.append(int(symbol))

        return stack[0]