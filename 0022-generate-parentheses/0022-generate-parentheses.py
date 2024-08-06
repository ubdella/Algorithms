class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(openLeft, closedLeft, s):
            if not openLeft and not closedLeft: 
                res.append(s)
                return
            
            if openLeft:
                dfs(openLeft - 1, closedLeft + 1, s + '(')

            if closedLeft:

                dfs(openLeft, closedLeft - 1, s + ')')

        res = []

        dfs(n, 0, '')

        return res
