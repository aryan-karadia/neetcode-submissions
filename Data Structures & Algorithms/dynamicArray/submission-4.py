class DynamicArray:
    

    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity: int = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        for index, item in enumerate(self.arr):
            if (item is not None):
                continue
            
            self.arr[index] = n
            print("adding inplace")
            print(self.arr)
            return

        print("array is full so appending")
        # if we made it here then array was full
        self.resize()
        self.pushback(n)


    def popback(self) -> int:
        for i in range(self.capacity - 1, -1, -1):
            if (self.arr[i] is not None):
                temp = self.arr[i]
                self.arr[i] = None
                return temp
 

    def resize(self) -> None:
        for i in range(self.capacity):
            self.arr.append(None)
        self.capacity *= 2
        print("done resizing!")

    def getSize(self) -> int:
        size = 0
        for x in self.arr:
            if x is not None:
                size += 1
        print("returning size!", size)
        return size
    
    def getCapacity(self) -> int:
        print("returning capacity:", self.capacity)
        return int(self.capacity)