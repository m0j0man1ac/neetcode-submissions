class Solution:
    #using hash map, is wrong
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen: dict[int, list[int]] = {}

        for i, n in enumerate(numbers):
            if n in seen:
                seen[n].append(i)
            else:
                seen[n] = [i]

        for n in seen:
            x = target - n
            """
            if x == n and len(seen[x]) >= 2:
                return [seen[n][0], seen[n][1]]
            """

            if x in seen:
                return [seen[n][0]+1, seen[x][0]+1]
            
        return []