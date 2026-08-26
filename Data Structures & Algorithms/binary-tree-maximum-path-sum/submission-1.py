# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            if node is None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            l = max(l, 0)
            r = max(r, 0)
            

            nonlocal res
            res = max(res, node.val + l + r)
            return node.val + max(l, r)
        
        dfs(root)
        return res
        

