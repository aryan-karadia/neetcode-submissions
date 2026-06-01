class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        if (self.head is None):
            return -1
        curIndex = 0
        node = self.head
        while(node is not None):
            if curIndex == index:
                return node.val
            node = node.nextNode
            curIndex += 1
        return -1
        

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.nextNode = self.head
        self.head = node
        
        

    def insertTail(self, val: int) -> None:
        node = self.head
        if node is None:
            self.head = Node(val)
            return
        while(node.nextNode is not None):
            node = node.nextNode
        node.nextNode = Node(val)
        

    def remove(self, index: int) -> bool:
        if (self.head is None):
            return False
        if (index == 0):
            self.head = self.head.nextNode
            return True
        curIndex = 1
        lastNode = self.head
        node = lastNode.nextNode
        while(node is not None):
            if curIndex == index:
                lastNode.nextNode = node.nextNode
                return True
            lastNode = lastNode.nextNode
            node = node.nextNode
            curIndex += 1
        return False
        

    def getValues(self) -> List[int]:
        vals = []
        node = self.head
        while(node is not None):
            vals.append(node.val)
            node = node.nextNode
        return vals
        

class Node:
    nextNode = None
    val = None
    def __init__(self, val = None):
        self.nextNode = None
        self.val = val
