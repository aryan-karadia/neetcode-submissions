# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()

        if list1 == None and list2 == None:
            return None
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        print("list1.val < list2.val", list1.val, list2.val)
        if list1.val < list2.val:
            # start with list1
            res.val = list1.val
            list1 = list1.next
        else:
            res.val = list2.val
            list2 = list2.next

        tmp = res
        while tmp:
            print(tmp.val)
            tmp = tmp.next
        
        print("before while loop\n\n")

        head = res
        while list1 or list2:
            res.next = ListNode()
            res = res.next

            if list1 is None:
                if list2:
                    res.val = list2.val
                    list2 = list2.next
                    continue
            
            if list2 is None:
                if list1:
                    res.val = list1.val
                    list1 = list1.next
                    continue
            # print("after checks", list1.val < list2.val)
            if list1.val < list2.val:
                res.val = list1.val
                list1 = list1.next
            else:
                res.val = list2.val
                list2 = list2.next         
            
        
        return head