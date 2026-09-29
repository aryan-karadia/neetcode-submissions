class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key = sorted(s1)

        left, right = 0, len(s1)
        while right <= len(s2):
            window = s2[left:right]
            if sorted(window) == key:
                return True
            left += 1
            right += 1
        
        return False
