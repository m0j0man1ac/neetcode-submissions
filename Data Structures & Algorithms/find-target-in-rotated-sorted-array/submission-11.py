class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        l,r = 0, size-1

        #if size <=2:
        #    for i,n in enumerate(nums):
        #        if n == target:
        #            return i


        while l<=r:
            mid = l + (r-l)//2
            n = nums[mid]

            #print(f"left {l} mid {mid} right {r}")

            if target == n:
                return mid
            
            #left is regularly sorted
            if nums[l] <= n:
                # in left clean window
                if nums[l] <= target < n:
                    r = mid-1
                else:
                    l = mid+1
            #inflection point to the left
            #right is sorted normally
            else:
                #in the sorted window to right
                if n < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1

        return -1
            


        