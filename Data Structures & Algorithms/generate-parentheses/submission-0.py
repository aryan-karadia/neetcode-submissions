class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(opened, closed, path):
            if opened == n and closed == n:
                res.append(path[:])
                return
            
            if opened > n or closed > n or closed > opened:
                return
            
            # decision 1 adding open
            path += ("(")
            backtrack(opened + 1, closed, path)
            path = path[:-1]

            # add closed
            path += (")")
            backtrack(opened, closed + 1, path)

        backtrack(1, 0, "(")

        return res
            
            
