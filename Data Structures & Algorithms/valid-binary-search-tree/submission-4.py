# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node, upper, lower):
            if not node:
                return True 

            if lower >= node.val or upper <= node.val:
                return False

            left = dfs(node.left, node.val, lower)
            lower = node.val
            right = dfs(node.right, upper, node.val)

            return (left and right)

        return dfs(root, 1001, -1001)
        