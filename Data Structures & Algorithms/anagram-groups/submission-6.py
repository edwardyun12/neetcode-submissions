class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        
        for txt in strs:
            newTxt = "".join(sorted(txt))
            if newTxt not in seen:
                seen[newTxt] = []
            
            seen[newTxt].append(txt)

        return list(seen.values())