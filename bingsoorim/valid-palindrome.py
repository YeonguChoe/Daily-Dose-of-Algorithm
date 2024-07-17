class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            # using built-in functions
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
