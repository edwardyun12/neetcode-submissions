class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_s = sorted(nums)
        baseNum = 0
        res = []

        for i in range(len(num_s)-2):
            if i > 0 and num_s[i] == num_s[i-1]:
                continue
            l , r = i + 1, len(num_s) - 1
            while l < r:
                addedNum = num_s[i] + num_s[l] + num_s[r]

                if addedNum > 0:
                    r -= 1
                elif addedNum < 0:
                    l += 1
                elif addedNum == 0:
                    res.append([num_s[i] ,num_s[l] , num_s[r]])

                    l += 1
                    r -= 1
                    while l < r and num_s[l] == num_s[l - 1]:
                        l += 1
        return res





       


                    
