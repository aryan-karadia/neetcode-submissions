from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        keyFreq = defaultdict(int)
        for char in t:
            keyFreq[char] += 1

        window = defaultdict(int)

        have, need = 0, len(keyFreq)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in keyFreq and window[c] == keyFreq[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in keyFreq and window[s[l]] < keyFreq[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""        

