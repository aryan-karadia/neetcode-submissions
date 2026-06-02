# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        if length == 1:
            return None
        
        if length == 2:
            if n == 2:
                # remove head
                head = head.next
            else:
                head.next = None
            return head

        if length == n:
            # remove head
            head = head.next
            return head

        prev, rmv = None, head
        for _ in range(1, length - (n - 1)):
            prev = rmv
            rmv = rmv.next
        
        tmp = rmv
        prev.next = tmp.next
        del rmv

        return head