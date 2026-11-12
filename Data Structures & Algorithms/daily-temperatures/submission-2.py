class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        [30,38,30,36,35,40,28]
        [0, 1, 2, 3, 4, 5, 6]
        st =[]
        result = [0]*len(temperatures)

        for t in range(len(temperatures)):
            
            
            
            while st and temperatures[t] > temperatures[st[-1]]:
                
                
                prev = st.pop()
                result[prev] = t - prev
                

            st.append(t)

        return result

                





                    