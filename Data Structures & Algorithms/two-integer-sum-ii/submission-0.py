class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1

        while l < r:
            addedNum = numbers[l] + numbers[r]
            if addedNum > target:
                # 1 + 4 < 3 
                r -= 1
            elif addedNum < target:
                l += 1
                # 1+ 4

            elif addedNum == target:
                return [l+1,r+1]
                
        
        