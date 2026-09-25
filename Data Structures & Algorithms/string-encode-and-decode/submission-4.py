class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "__empty__"
        res = []
        for s in strs:
            encoded = ""
            if len(s) == 0:
                res.append("\x00")
                continue
            for c in s:
                encoded += chr(ord(c) + 1)
            res.append(encoded)
        return "\x1f".join(res)

    def decode(self, s: str) -> List[str]:
        if s == "__empty__":
            return []
        if len(s) == 0:
            return [""]
        chunks = s.split("\x1f")
        res = []
        
        for chunk in chunks:
            if chunk == "\x00":
                res.append("")
                continue
            
            word = ""
            for c in chunk:
                word += chr(ord(c) - 1)
            res.append(word)
        
        return res

