class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = collections.defaultdict(list)
        for c, p in prerequisites:
            adjMap[c].append(p)

        seen = set()
        def dfs(course):
            if course in seen:
                return False
            preReqs = adjMap[course]

            if len(preReqs) == 0:
                return True

            seen.add(course)
            for pre in preReqs:
                if not dfs(pre): return False
            seen.remove(course)
            adjMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True