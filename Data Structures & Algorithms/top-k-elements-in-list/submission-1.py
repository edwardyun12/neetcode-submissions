class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        # 예: Counter({1: 3, 2: 2, 3: 1})
        
        # 1. counts.most_common(k) 실행 결과 -> [(1, 3), (2, 2)] (숫자, 빈도수) 튜플 형태
        # 2. 여기서 숫자(num)만 꺼내서 리스트로 만듭니다.
        res = []
        for num, count in counts.most_common(k):
            res.append(num)
            
        return res
        
