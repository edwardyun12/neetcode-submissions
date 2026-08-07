class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        
        print(sorted(counts, key=counts.get, reverse= True))
        
        for i in sorted(counts, key=counts.get, reverse= True):
            res.append(i)
            if len(res) == k:
                break
        
        return res
