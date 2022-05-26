class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        hashmap = {
            "+":    True,
            "-":    True,
            "*":    True,
            "/":    True
        }
        for token in tokens:
            if token in hashmap:
                v1 = stack.pop()
                v2 = stack.pop()
                if token == "+":
                    res = v1 + v2
                elif token == "-":
                    res = v2 - v1
                elif token == "*":
                    res = v2 * v1
                else:
                    res = int(v2 / v1)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]
                
                
        