class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3

    # [7, 4, 1, 0]

    # car_map = {position: speed}
    # [(10-0)/1, ...]
    # [3, 3, >4, 10]

        car_map = {}
        stack = []
        for n in range(len(position)):
            car_map[position[n]] = speed[n]
        position.sort(reverse=True)

        for p in position:
            curr = (target - p ) / car_map[p]
            if not stack or stack[-1] < curr:
                stack.append(curr)
        return len(stack)


























        # stack = []
        # cars = sorted(zip(position,speed), reverse=True)

        # for po, spe in cars:
        #     fleet = (target - po) / spe
        #     if not stack or fleet > stack[-1]:
        #         stack.append(fleet)
        # return len(stack)