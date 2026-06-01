from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque([root])

        while len(q) > 0:
            first = q.popleft()
            # swap
            first.left, first.right = first.right, first.left
            if first.left is not None:
                q.append(first.left)
            if first.right is not None:
                q.append(first.right)
        
        return root