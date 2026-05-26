class Solution:
    def isValid(self, s: str) -> bool:
        size = len(s)
        if not size%2 == 0:
            return False

        stack = []
        openBDict = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c in ['{', '[', '(']: #open bracket, add to stack
                stack.append(c)
                continue

            if stack:
                if stack[-1] == openBDict[c]:
                    stack.pop()
                    continue

            return False

        return len(stack) == 0
