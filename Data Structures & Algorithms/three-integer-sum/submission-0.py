class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []
        baseNum = 0

        for i in range(len(sortedNums)):
            l , r = baseNum + 1 , len(sortedNums) -1
            while l < r:

                addedNum = sortedNums[baseNum] + sortedNums[l] + sortedNums[r]
                if addedNum > 0:
                    r -= 1
                elif addedNum <0:
                    l += 1
                elif addedNum == 0:
                    if [sortedNums[baseNum], sortedNums[l], sortedNums[r]] not in res:
                        res.append([sortedNums[baseNum], sortedNums[l], sortedNums[r]])
                    l += 1
                    r -= 1
            
            baseNum += 1    
        return(res)
       


                    
