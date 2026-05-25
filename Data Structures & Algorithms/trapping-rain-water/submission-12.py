class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        size = len(height)
        
        # Pre-build suffix array using a reversed running maximum
        # Doing this without manual index lookups runs at maximum C-speed
        suffixTallest = [0] * size
        current_max = 0
        for i in range(size - 1, -1, -1):
            if height[i] > current_max:
                current_max = height[i]
            suffixTallest[i] = current_max
            
        total_water = 0
        prefix_max = 0
        
        # Calculate water on the fly in a single pass
        # This completely eliminates the need for the volAtI array
        for i in range(size):
            if height[i] > prefix_max:
                prefix_max = height[i]
            
            # Water at i is simply the min of left/right caps minus current floor
            total_water += min(prefix_max, suffixTallest[i]) - height[i]
            
        return total_water