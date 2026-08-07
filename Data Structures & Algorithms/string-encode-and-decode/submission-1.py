class Solution:

    def encode(self, strs: List[str]) -> str:
        resList = []
        for txt in strs:
            resList.append(str(len(txt)) + "#" + txt)
        
        return "".join(resList)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
        
            txtLength = int(s[i:j])

            res.append((s[j + 1: j + 1 + txtLength]))

            i = j + 1 + txtLength

        return res
       