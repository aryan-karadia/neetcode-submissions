"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited_vals = dict()
        def dfs(val, original):
            if val in visited_vals.keys():
                return visited_vals[val]
            
            # add to visited
            newNode = Node(val)
            visited_vals[val] = newNode

            for n in original.neighbors:
                neigh = dfs(n.val, n)
                newNode.neighbors.append(neigh)
            
            return newNode
        
        return dfs(node.val, node)



