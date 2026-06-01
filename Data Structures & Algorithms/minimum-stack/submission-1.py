class MinStack:
    stack = []
    prefixStack = []

    def __init__(self):
        self.stack = []
        self.prefixStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        prefixN = len(self.prefixStack)
        if prefixN == 0:
            self.prefixStack.append(val)
        else:
            minVal = min(val, self.prefixStack[prefixN - 1])
            self.prefixStack.append(minVal)

    def pop(self) -> None:
        self.prefixStack.pop()
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.prefixStack[len(self.prefixStack) - 1]
        
