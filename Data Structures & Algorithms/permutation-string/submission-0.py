class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        if len(s1) == 1:
            return s1 in s2

        key = "".join(sorted(s1))

        left, right = 0, len(s1) - 1

        while right < len(s2):
            sortedWindow = "".join(sorted(s2[left:right + 1]))
            if sortedWindow == key:
                return True
            else:
                left += 1
                right += 1
        
        return False
        