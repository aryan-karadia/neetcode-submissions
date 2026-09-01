from collections import deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Include ALL unique characters in the dictionary initially
        adj = {c: set() for w in words for c in w}
        in_degree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # FIX 1: Invalid prefix ordering check (e.g., "abc" before "ab")
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            j = 0
            while j < len(word1) and j < len(word2):
                if word1[j] != word2[j]:
                    # FIX 2: Store graph edges properly and track in-degrees
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
                j += 1
            
        # FIX 3: Topological Sort using Kahn's Algorithm instead of linear traversal
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        res = []

        while queue:
            cur = queue.popleft()
            res.append(cur)
            for neighbor in adj[cur]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Return result if all unique characters were ordered; otherwise cycle exists
        return "".join(res) if len(res) == len(adj) else ""