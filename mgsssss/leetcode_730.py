class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, val in enumerate(temperatures):
            while len(stack) > 0 and val > stack[-1][1]:
                last_index, last_val = stack.pop()
                res[last_index] = index - last_index
            stack.append((index, val))
        return res