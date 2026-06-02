# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calcHeight(root)

        return self.res

    def calcHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        maxLeft = self.calcHeight(root.left)
        maxRight = self.calcHeight(root.right)
        
        self.res = max(self.res, maxLeft + maxRight)

        return max(maxLeft, maxRight) + 1

