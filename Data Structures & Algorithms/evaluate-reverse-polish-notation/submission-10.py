class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["+", "-", "*", "/", "//", "%", "**"]
        stack = []
        for t in tokens:
            if t in op:
                fir = stack.pop()
                sec = stack.pop()
                new_res = 0
                if t == "+":
                    new_res = fir + sec
                elif t == "-":
                    new_res = sec - fir
                elif t =="*":
                    new_res = fir * sec
                elif t =="/":
                    new_res = int(sec / fir)
                stack.append(new_res)

            else:
                stack.append(int(t))
        return stack[-1]
