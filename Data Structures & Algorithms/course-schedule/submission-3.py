class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjs = defaultdict(list)
        for a, b in prerequisites:
            adjs[a].append(b)
        
        courseWeCanTake = set()
        # return true if you can take it
        # false otherwise
        def dfs(course, visited):
            if course in visited:
                return False
            if len(adjs[course]) == 0 or course in courseWeCanTake:
                return True
            
            # explore all prereqs
            visited.add(course)
            canTake = True
            for prereq in adjs[course]:
                canWeTakeChildCourse = dfs(prereq, visited)
                canTake = canTake and canWeTakeChildCourse
                if canWeTakeChildCourse:
                    courseWeCanTake.add(prereq)
            
            visited.remove(course)
            return canTake
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
            else:
                courseWeCanTake.add(i)
        
        return True
            

