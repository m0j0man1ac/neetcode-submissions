class Solution:
    def findMin(self, nums: List[int]) -> int:
        size  = len(nums)
        lasti = size-1

        l, r = 0, lasti

        while l<=r:
            mid = l + (r-l)//2
            n = nums[mid]

            #get 1 left index from mid, accounting for rotation
            #if its larger, current num in min
            previ = lasti if mid == 0 else mid-1
            if nums[previ] >= n:
                return n

            #inflection to right
            if n > nums[r]:
                l = mid+1
            #its not
            else:
                r = mid-1

        return -1