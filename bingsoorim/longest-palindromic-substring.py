class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force: check every single possible substring; O(n^3)
        # using two pointers: foreach char in str, expand the pointers to check pali; O(n^2)
        # res = ""
        # resLen = 0

        # for i in range(len(s)):
        #     # odd length
        #     l, r = i, i # center position
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r-l+1) > resLen:
        #             # longer than the current res, update it
        #             res = s[l:r+1]
        #             resLen = r-l+1
        #         l -= 1
        #         r += 1
        #     # even length
        #     l, r = i, i+1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r-1+1) > resLen:
        #             res = s[l:r+1]
        #             resLen = r-l+1
        #         l -= 1
        #         r += 1
                
        # return res
        
        # DP
        dp = [[False]*len(s) for _ in range(len(s))]
        ans = [0,0]

        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i,i+1]

        for diff in range(2, len(s)):
            for i in range(len(s) - diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i,j]
        
        i,j = ans
        return s[i:j+1]
