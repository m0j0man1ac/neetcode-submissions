class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)

        l = 0
        r = size-1

        print(f"size {size}")

        while l <= r:
            mid = (l+r)//2
            n = nums[mid]

            if n == target:
                return mid

            if n < target: #larger half
                l = mid+1
            else: #smaller half
                r = mid-1
            
            print(mid)

        return -1;
        