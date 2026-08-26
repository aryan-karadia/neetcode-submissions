# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        heap = []
        
        for lst in lists:
            temp = lst
            while temp:
                heapq.heappush(heap, temp.val)
                temp = temp.next
        
        while len(heap) > 0:
            newNode = ListNode(heapq.heappop(heap))
            cur.next = newNode
            cur = cur.next
        
        return dummy.next