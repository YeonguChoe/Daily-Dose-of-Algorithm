from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # simple solution would be sorting each item in the list and group anagrams: O(m*nlogn)
        # more efficient solution is using a hashmap: O(m*n*26)
        # Defining a dictionary with values as a list
        res = defaultdict(list) # mapping charCount to list of anagrams
        for s in strs:
            count = [0] * 26 # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1 # using the ASCII values
            
            res[tuple(count)].append(s)
        
        return res.values()
