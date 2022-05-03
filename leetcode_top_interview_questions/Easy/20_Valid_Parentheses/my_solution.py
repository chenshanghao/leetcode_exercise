class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if char == ')' and top == '(':
                    pass
                elif char == ']' and top == '[':
                    pass
                elif char == '}' and top == '{':
                    pass
                else:
                    return False
        return True if len(stack) == 0 else False
            
