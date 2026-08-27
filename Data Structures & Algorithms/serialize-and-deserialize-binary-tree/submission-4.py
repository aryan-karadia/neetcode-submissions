class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []

        def dfs(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            val = vals[self.i]
            if val == "#":
                self.i += 1
                return None
            node = TreeNode(int(val))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()