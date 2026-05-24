class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences: dict[int, int] = {}
        for x in nums:
            if x not in occurences:
                occurences[x] = 1
            else:
                return True

        return False

# should instead use 'seen = set()'
# hashset with only keys

        