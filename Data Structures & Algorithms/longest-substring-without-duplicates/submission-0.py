class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLength = 1
        left = 0
        for right in range(1, len(s)):
            subStr = s[left:right]
            while s[right] in subStr:
                left += 1
                subStr = s[left:right]
            maxLength = max(maxLength, len(subStr) + 1)
        
        return maxLength