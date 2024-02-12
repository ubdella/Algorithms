class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for para in s:
            if para == '(' or para == '[' or para == '{':
                stack.append(para)
            elif para == ')' or para == ']' or para == '}' :
                if not stack:
                    return False
                top = stack.pop()
                if para == ')':
                    if top != '(':
                        return False
                elif para == '}':
                    if top != '{':
                        return False
                elif para == ']':
                    if top!='[':
                        return False
        return not stack
                    
                
                
            