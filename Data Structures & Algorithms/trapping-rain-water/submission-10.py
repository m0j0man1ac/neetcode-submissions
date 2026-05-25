class Solution:
    #prefix and suffix solution
    def trap(self, height: List[int]) -> int:
        size = len(height)
        
        prefixTallest = [0] * size
        prefixTallest[0] = height[0]

        suffixTallest = [0] * size
        suffixTallest[0] = height[size-1]

        preT = -1
        sufT = -1

        for i in range(size):
            j = size - 1 - i

            preT = max(preT, height[i])
            sufT = max(sufT, height[j])
            
            prefixTallest[i] = preT
            suffixTallest[j] = sufT
        
        volSum = 0

        for i in range(size):
            vol = min(prefixTallest[i], suffixTallest[i]) - height[i]
            volSum += vol


        return volSum