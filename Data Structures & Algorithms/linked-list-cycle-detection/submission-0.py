# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        seen = []
        iterator = head

        while iterator:
            if iterator in seen:
                return True
            
            seen.append(iterator)
            iterator = iterator.next
        
        return False
