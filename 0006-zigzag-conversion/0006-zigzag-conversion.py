class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        # PAYPALISHIRING
        dire = 'down'
        i,j = 0,0
        grid = [['']*len(s) for _ in range(numRows)]
        for sIndex in range(len(s)):
            
            grid[i][j] = s[sIndex]
            if dire == 'down':
                if i == numRows - 1:
                    dire = 'up'
                    i -= 1
                    j += 1
                else:
                    i += 1
            else:
                if i == 0:
                    dire = 'down'
                    i += 1
                else:
                    i -= 1
                    j += 1
        result = ''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '':
                    result += grid[i][j]
        return result
