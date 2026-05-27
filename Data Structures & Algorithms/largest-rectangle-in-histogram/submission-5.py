class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        stack = []

        largest = 0

        top = (heights[0], 1)
        i=1

        #build stack, high points are calculated and discarded as we go
        while i < size:
            if heights[i] == top[0]:
                top = (top[0], top[1]+1)
            elif heights[i] < top[0]:
                largest = max(top[0]*top[1], largest)
                #print(top)
                if len(stack)>0 and stack[-1][0] > heights[i]: #trick tricky, only add width behind you if the width wont be recieved from the next rectangle on the back pass
                    old = stack.pop()
                    stack.append((old[0], old[1] + top[1]))
                top = (heights[i], 1 + top[1]) #tricky tricky
            elif heights[i] > top[0]:
                stack.append(top)
                top = (heights[i], 1)

            i += 1

        stack.append(top)

        #print(largest)
        #print(stack)

        #traverse through stack to consume
        cur = stack.pop()
        while len(stack) > 0:
            print(cur)
            largest = max(largest, cur[0]*cur[1])
            next = stack.pop()
            if cur[0] >= next[0]: #if next rect is smaller, pass on width
                cur = (next[0], next[1] + cur[1])
            else:
                cur = next

        largest = max(largest, cur[0]*cur[1])

        return largest
