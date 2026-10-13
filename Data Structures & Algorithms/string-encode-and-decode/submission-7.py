class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (f"{len(s)}#{s}")
        
        return res
        
    # 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            r = i
            while s[r] != '#':
                r += 1
            
            stringLength = int(s[i:r])

            i = r + 1

            res.append(s[i: i + stringLength])

            i += stringLength
        
        return res

        

