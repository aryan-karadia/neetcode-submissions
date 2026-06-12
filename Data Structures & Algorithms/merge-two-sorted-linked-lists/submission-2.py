# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = r = None
        if list1 is None and list2 is None:
            return list1
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            l = list1
            r = list2
        else:
            l = list2
            r = list1

        res = l
        
        while l.next and r:
            if r.val < l.next.val:
                tmp = r.next
                r.next = l.next
                l.next = r
                r = tmp
            l = l.next
        
        if r:
            l.next = r
        
        return res

            