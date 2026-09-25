# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kNode = self.findKNode(groupPrev, k)
            if not kNode:
                # leave as is
                break
            groupNext = kNode.next

            prev, curr = kNode.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kNode
            groupPrev = tmp
        
        return dummy.next
        


    def findKNode(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node 


        