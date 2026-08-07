class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []

        numCount = sorted(counts.keys(), key=counts.get, reverse=True)

        for i in numCount:
            res.append(i)
            if len(res) == k:
                break
        return res
        """
        // Way 1
        res = []

        for i, nums in counts.most_common(k):
            res.append(i)
        
        return res"""


