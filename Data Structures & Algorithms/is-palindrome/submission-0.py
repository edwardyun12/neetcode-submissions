class Solution:
    def isPalindrome(self, s: str) -> bool:
        newTxt = []
        
        for char in s:
            if char.isalnum():
                newTxt.append(char.lower())
        
        return newTxt == newTxt[::-1]
