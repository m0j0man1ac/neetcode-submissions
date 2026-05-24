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
                """
                if j == i:
                    continue
                """

                visited = {n:seen[n]-1}
                visited[jn] = visited.get(jn, seen[jn])-1
                if visited[jn] < 0:
                    continue
                
                """
                print(f"{n}:{jn}")
                print(visited)
                print("")
                """

                x = 0 - (jn + n)

                isATriplet = False

                #one of active values, has duplicate
                if x in visited:
                    if visited.get(x, 0) >= 1:
                        isATriplet = True
                #all unique
                elif x in seen:
                    isATriplet = True

                if isATriplet:
                    sortedL = sorted([n, jn, x])
                    results.add(tuple(sortedL))
                

        return list(results)