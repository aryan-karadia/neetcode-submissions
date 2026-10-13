class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        stack.append(0)
        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                oldI = stack.pop()
                res[oldI] = i - oldI
            else:
                stack.append(i)
        
        return res