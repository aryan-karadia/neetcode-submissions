class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node, par):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                dfs(nei, node)
        
        count = 0
        for n in range(n):
            if n not in visit:
                count += 1
                dfs(n, -1)

        return count
            