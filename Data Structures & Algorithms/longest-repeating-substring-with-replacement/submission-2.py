class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        maxVal = 0
        for char in set(s):
            l, r = 0, 0
            usedK = 0
            while r < len(s):
                if s[r] == char:
                    r += 1
                elif usedK < k:
                    usedK += 1
                    r += 1
                else:
                    if s[l] != char:
                        usedK -= 1
                    l += 1
                maxVal = max(maxVal, r - l)
        return maxVal