class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        res = []

        for i, nums in counts.most_common(k):
            res.append(i)
        
        return res
