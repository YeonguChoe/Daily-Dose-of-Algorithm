'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
2024-07-27

backtracking의 대표적인 문제
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers_dict = {"2":["a","b","c"],"3":["d","e","f"], "4":["g","h", "i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        res = []
        def backtracking(index, curr):
            if len(curr) == len(digits):
                res.append("".join(curr[:]))
                return
            
            for str in numbers_dict[digits[index]]:
                curr.append(str)
                backtracking(index+1, curr)
                curr.pop()
                
        if digits:
            backtracking(0, [])
        return res