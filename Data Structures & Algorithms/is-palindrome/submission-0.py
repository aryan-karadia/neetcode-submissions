class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        sanitized = ""
        for c in s:
            if c.isalnum():
                if not c.isnumeric():
                    sanitized += (c.lower())
                else:
                    sanitized += c
        
        l, r = 0, len(sanitized) - 1

        while l < r:
            if sanitized[l] != sanitized[r]:
                return False
            l += 1
            r -= 1
        
        return True