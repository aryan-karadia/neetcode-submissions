# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)

        if not p and not q:
            return True
        
        if (p and not q) or (not p and q):
            return False

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if node1.val != node2.val:
                print(f"node1.val: {node1.val} and node2.val: {node2.val}")
                return False
            
            if node1.left and node2.left:
                q1.append(node1.left)
                q2.append(node2.left)

            if (node1.left and not node2.left) or (not node1.left and node2.left):
                return False
            
            if node1.right and node2.right:
                q1.append(node1.right)
                q2.append(node2.right)
            
            if (node1.right and not node2.right) or (not node1.right and node2.right):
                return False


        if len(q1) != 0 or len(q2) != 0:
            return False
        return True