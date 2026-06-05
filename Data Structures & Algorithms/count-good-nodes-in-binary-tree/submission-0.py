# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    def goodNodes(self, root: TreeNode) -> int:
        seen = [root.val]
        def dfs(node):
            if not node:
                return

            elif node.val >= max(seen):
                self.count += 1
            
            seen.append(node.val)
            dfs(node.left)
            dfs(node.right)
            seen.pop()
        
        dfs(root)

        return self.count


             