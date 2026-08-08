class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * n
        right = [1] * n
        res = [1] * n

        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
            # 1. [1,1,1,1] i = 1
            # 2. [1,1,2,1] i = 2
            # 3. [1,1,2,8] i = 3 Final


        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            # n = 4
            # 1. [1,1,6,1] i=2
            # 2. [1,24,6,1] i=1
            # 3. [48,24,6,1] i=0

        for i in range(n):
            res[i] = left[i] * right[i]
        
        return res

        