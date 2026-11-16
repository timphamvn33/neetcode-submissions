class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # fast -> slow
    # slow -> fast 

    # we need to find the numbe of fast car that behind the fast car then we can total the car fleet

    # target = 10, position = [4,1,0,7], speed = [2,2,1,1]

    # speed = s/t -> t = s/speed

    # 7 -> 3 +
    # 0 -> 10
    # 1 -> 9/2 
    # 4 -> 6/2 +

    # find the nearest car -> max_position
    # 7, 4, 1, 0
        st = []
        cars = sorted(zip(position, speed), reverse=True)

        for p, s in cars:
            t = (target - p)/s
            if not st:
                st.append(t)
            
            elif st[-1] < t:
                st.append(t)
        return len(st)



        # max_postion = 0
        # max_time = 0
        # st = []

        # for i, p in enumerate(position):
        #     if max_postion < p:
        #         max_postion = p
        #         max_time = (target-max_postion)/speed[i]


        # for i in range(len(position)):
        #     st.append(position[i])
        #     curr_time = (target-st[-1])/speed[i]
        #     if (curr_time > max_time):
        #         st.pop()

        return len(st)

        

        