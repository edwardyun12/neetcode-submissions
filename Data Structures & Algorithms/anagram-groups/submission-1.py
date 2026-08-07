class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            txt = "".join(sorted(i))
            if txt not in seen:
                seen[txt] = []
            
            seen[txt].append(i)
        return list(seen.values())

            

            