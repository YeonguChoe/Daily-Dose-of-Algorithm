class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # using two pointers, find the subsequences
        sp = tp = 0
         
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == len(s)
