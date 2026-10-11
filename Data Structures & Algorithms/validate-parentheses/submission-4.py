class Solution:
    def isValid(self, s: str) -> bool:
        map_closed = {")": "(", "}": "{", "]": "["}
        stack = [];
        for c in s:
            if c in map_closed:
                if not stack or stack[-1] != map_closed[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0