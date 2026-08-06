class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        joined = list(zip(position, speed))
        joined.sort()
        joined.reverse()
        stack = []

        for pos, speed in joined:
            eta = (target - pos) / speed
            if not stack:
                stack.append(eta)
            currEta = stack[-1]
            if eta > currEta:
                    stack.append(eta)

        return len(stack)
