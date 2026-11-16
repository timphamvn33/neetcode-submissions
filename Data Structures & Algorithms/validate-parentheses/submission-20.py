class Solution:
    def isValid(self, s: str) -> bool:
        mp = {")": "(", "]": "[", "}": "{"}

        stack = []

        for c in s:
            
            if c in mp:

                

                if stack and mp[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

            

        if len(stack) == 0 :
            return True
        else:
            return False
            
