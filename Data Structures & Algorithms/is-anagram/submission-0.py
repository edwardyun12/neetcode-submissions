class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstDict = {}
        secondDict = {}

        for i in s:
            if i not in firstDict:
                firstDict[i] = 1
            else:
                firstDict[i] += 1

        for j in t:
            if j not in secondDict:
                secondDict[j] = 1
            else:
                secondDict[j] += 1

        return firstDict == secondDict  
            
            
        