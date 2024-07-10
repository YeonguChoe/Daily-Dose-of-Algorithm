class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # dealing with an order of elements
        answers = [0] * len(temperatures) # initialize the answers
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                answers[idx] = i - idx
            stack.append(i)
        
        return answers
