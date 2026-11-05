class Solution:
    def isValid(self, s: str) -> bool:
        close_par = {
            "}": "{", ")": "(", "]": "["
            }
        stack = []
        for c in s:
            if c in close_par:
                if not stack or stack[-1] != close_par[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0

        

        

        