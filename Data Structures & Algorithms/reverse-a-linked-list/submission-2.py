# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = None
        curr = head
        nxt = curr.next
        curr.next = prev

        while nxt.next is not None:
            temp = nxt.next
            # reverse
            nxt.next = curr

            # move forward
            prev = curr
            curr = nxt
            nxt = temp

        nxt.next = curr
        return nxt