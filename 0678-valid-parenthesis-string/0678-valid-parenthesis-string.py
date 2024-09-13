class Solution:
    def checkValidString(self, s: str) -> bool:
        # First pass: left to right
        open_count = star_count = 0
        for char in s:
            if char == '(':
                open_count += 1
            elif char == '*':
                star_count += 1
            else:  # char == ')'
                if open_count > 0:
                    open_count -= 1
                elif star_count > 0:
                    star_count -= 1
                else:
                    return False
                
            closeCount = starCount = 0
            
            for i in range(len(s) - 1, -1, -1):
                c = s[i]
                if c == ')':
                    closeCount += 1
                elif c == '*':
                    starCount += 1
                else:
                    if closeCount > 0:
                        closeCount -= 1
                    elif starCount > 0:
                        starCount -= 1
                    else:
                        return False
        return True