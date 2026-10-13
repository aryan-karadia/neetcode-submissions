class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        res = 1
        l = 0
        for r in range(1, len(s)):
            subString = s[l:r]
            while s[r] in subString:
                l += 1
                subString = s[l:r]
            res = max(res, len(subString) + 1)
        
        return res


        