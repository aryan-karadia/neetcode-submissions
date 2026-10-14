class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.getter = {}
        self.least = Node(0, 0)
        self.most = Node(0, 0)
        self.maxCap = capacity
        self.least.next = self.most
        self.most.prev = self.least

    def get(self, key: int) -> int:
        if key in self.getter:
            self.remove(self.getter[key])
            self.insert(self.getter[key])

            return self.getter[key].val
        return -1
    
    def remove(self, node):
        temp = node
        prev, nextNode = temp.prev, temp.next
        prev.next = nextNode
        nextNode.prev = prev
        del temp
    
    #insert at most
    def insert(self, node):
        prev = self.most.prev
        node.prev = prev
        self.most.prev = node
        prev.next = node
        node.next = self.most 
        

    def put(self, key: int, value: int) -> None:
        if key in self.getter:
            self.remove(self.getter[key])
        
        self.getter[key] = Node(key, value)
        self.insert(self.getter[key])

        if len(self.getter) > self.maxCap:
            lru = self.least.next
            self.remove(lru)
            del self.getter[lru.key]
        





        
        
