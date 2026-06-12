"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        if not head:
            return head
        hashMap = {}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            hashMap[curr] = copy
            curr = curr.next
        
        copy = hashMap[head]
        curr = head
        while curr:
            if curr.next:
                copy.next = hashMap[curr.next]
            if curr.random is not None:
                copy.random = hashMap[curr.random]
            curr = curr.next
            copy = copy.next
        
        return hashMap[head]
        
