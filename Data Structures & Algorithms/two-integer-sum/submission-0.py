class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            needNum = target - num
            
            if needNum in seen:
                return [seen[needNum],i]
            
            seen[num]= i


        