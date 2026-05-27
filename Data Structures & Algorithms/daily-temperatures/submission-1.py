class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        size = len(t)

        stack = []
        result = [0] * size

        for i in range(size):
            #pop case
            while len(stack) > 0:
                if t[stack[-1]] < t[i]: #found a warmer day
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    break

            stack.append(i)    

        #things left in stack
        for i in stack:
            result[i] = 0

        return result

