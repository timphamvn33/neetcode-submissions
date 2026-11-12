class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ["+", "-", "*", "/"]
        

        for t in tokens:
            if t not in op:
                st.append(int(t))
                
            else:
                num1 = st.pop()
               
                num2 = st.pop()
                
                if t == "+":
                    new_num = num2 + num1
                    
                elif t == "-":
                    new_num = num2 - num1
                elif t == "*":
                    new_num = int(num1 * num2)
                else:

                    new_num = int(num2 / num1)
                
                st.append(new_num)
        return st.pop()
            
