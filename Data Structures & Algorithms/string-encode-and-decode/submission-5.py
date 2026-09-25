class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            
            res.append(f"{len(s)}#{s}")
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            start = j + 1
            res.append(s[start: start + length])
            i = start + length
        
        return res

