class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx: dict[int, int] = {}

        for i, n in enumerate(nums):
            dif = target - n

            if dif in num_idx:
                return [num_idx[dif], i]
            
            num_idx[n] = i

        return []