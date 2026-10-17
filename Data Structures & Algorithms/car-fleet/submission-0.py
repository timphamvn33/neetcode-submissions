class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position,speed), reverse=True)

        for po, spe in cars:
            fleet = (target - po) / spe
            if not stack or fleet > stack[-1]:
                stack.append(fleet)
        return len(stack)