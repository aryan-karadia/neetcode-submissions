class Node:
        def __init__(self, key, val):
            self.key, self.val = key, val
            self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.LRU = Node(0, 0)
        self.MRU = Node(0, 0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    # remove from list
    def remove(self, node):
        temp = node
        prev, nextNode = temp.prev, temp.next
        prev.next = nextNode
        nextNode.prev = prev
        del temp

    # insert at right
    def insert(self, node):
        prev = self.MRU.prev
        prev.next = node
        self.MRU.prev = node
        node.next = self.MRU
        node.prev = prev
        return

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # update most recent
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])

        self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.capacity:
            # remove LRU
            lru = self.LRU.next
            self.remove(lru)
            # delete from hashmap
            del self.hashmap[lru.key]
        
           


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)