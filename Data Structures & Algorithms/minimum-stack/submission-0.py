class MinStack:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        minVal = self.stack[0]
        for val in self.stack:
            if val < minVal:
                minVal = val
        
        return minVal
        
