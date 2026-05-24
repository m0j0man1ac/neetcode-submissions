class Solution:
    #O(n^2) using hash
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        seen: dict[int, int] = {}

        for n in nums:
            seen[n] = seen.get(n, 0) + 1

        seenList = list(seen.keys())

        """
        print(seen)
        print("")
        """

        results = set()

        for i, n in enumerate(seenList):
            for j in range(i, len(seenList)):
                jn = seenList[j]

                if n == jn and seen[n] < 2:
                    continue
                
                # print(f"{n}:{jn}")

                x = 0 - (jn + n)
                
                available_x = seen.get(x, 0)
                if n == x:
                    available_x -= 1
                if jn == x:
                    available_x -= 1

                if available_x > 0:
                    sortedL = sorted([n, jn, x])
                    results.add(tuple(sortedL))
                    
                    # print(sortedL)
                    
                # print("")
                

        return list(results)