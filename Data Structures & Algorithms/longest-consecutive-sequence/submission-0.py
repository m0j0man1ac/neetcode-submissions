class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seenHash = set()
        visited = set()

        startIdx = 0
        longest = 0

        for n in nums:
            seenHash.add(n)

        for n in seenHash:
            if n in visited:
                continue

            visited.add(n)

            length = 1
            
            x = n-1
            #check back
            while(True):
                if not x in seenHash:
                    break
                
                visited.add(x)
                length += 1
                x -= 1

            x = n+1
            #check forward
            while(True):
                if not x in seenHash:
                    break

                visited.add(x)
                length += 1
                x += 1

            longest = max(longest, length)

        return longest