class Solution:
    def trap(self, height: List[int]) -> int:        
        totalV = 0

        i = 0
        while(i<len(height)-1):
            l = height[i]

            if l <= 0:
                i += 1
                continue

            j = i+1

            noMatch = False
            highestMatch = (-1,-1)
            heightSum = 0

            while j < len(height):
                r = height[j]
                if highestMatch[1] < r:
                    highestMatch = (j, r)
                
                if l > r:
                    heightSum += r
                    j += 1
                    if j == len(height):
                        noMatch = True
                    continue
                
                vol = min(l, r) * (j-i-1) - heightSum
                #print(f"testing pair - idx {i}:{j} h {height[i]}:{height[j]} - vol {vol} (-{heightSum})")
                totalV += vol
                break

            if noMatch:
                highI, highN = highestMatch
                if not highN <= 0:
                    sumHeights = sum(height[i + 1 : highI])
                    """
                    for x in range(i+1, highI):
                        sumHeights += height[x]
                    """
                    vol = min(height[i], height[highI]) * (highI-i-1) - sumHeights
                    totalV += vol
                    
                    i = highI
                else: #exit, all remaining entries are 0
                    i=len(height)+1
            else:
                i = j
            
        return totalV