class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = s.strip().split() # trailing whitespaces, then split into words

        if not w:
            # if there is no words
            return 0
        
        return len(w[-1])
