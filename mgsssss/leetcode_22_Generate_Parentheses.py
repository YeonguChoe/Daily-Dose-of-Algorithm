'''
https://leetcode.com/problems/generate-parentheses/
2024-07-18

backtracking 변형 문제

nums = [1,2,3,4,5,6,7,8,9,10]

res = []
def backtracking(curr):
    if len(curr) == nums:
       res.append(curr[:]) 
       return
    for i in range(len(nums)):
        curr.append(nums[i])
        backtracking(curr)
        curr.pop()
backtracking([])
return res

해당 하는 코드를 암기하고 backtracking 관련된 문제가 나오면 응용해서 사용
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(curr, start, end):
            if start == n and end == n:
                res.append("".join(curr[:]))
                return
            
            if start < n:
                curr.append("(")
                backtracking(curr, start+1, end)
                curr.pop()
            if end < start:
                curr.append(")")
                backtracking(curr, start, end+1)
                curr.pop()
        
        backtracking([], 0, 0)
        return res