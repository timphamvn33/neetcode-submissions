class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        [30,38,30,36,35,40,28]
        [1, 4, 1, 2, 1, 0, 0]
        [0, 1, 2, 3, 4, 5, 6]

        st = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            
            
            while st and temperatures[i] > temperatures[st[-1]]:
                
                c = st.pop()
                
                result[c]= i-c
                
            st.append(i)
        return result

        
        