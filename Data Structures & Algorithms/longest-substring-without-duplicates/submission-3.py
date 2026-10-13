class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        res = 1
        left = 0
        for right in range(1, len(s)):
            subString = s[left:right]
            while s[right] in subString:
                left += 1
                subString = s[left:right]
            res = max(res, len(subString) + 1)
        
        return res