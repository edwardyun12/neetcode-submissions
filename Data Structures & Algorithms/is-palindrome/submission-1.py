class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = []
        
        for char in s:
            if char.isalnum():
                clean_s.append(char.lower())
        
        if clean_s == clean_s[::-1]:
            return True
        else:
            return False
        
