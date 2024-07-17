class Solution:
    def isValid(self, s: str) -> bool:
        # TC: O(n), SC: O(n)
        # hashmap to store the matching parentheses
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        # use stack to solve the problem
        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # open parentheses then just push into the stack
                stack.append(c)
        
        return True if not stack else False

