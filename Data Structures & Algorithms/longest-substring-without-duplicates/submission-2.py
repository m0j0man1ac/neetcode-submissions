class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen : dict[str:int] = {}
        start = 0
        longest = 0

        for i,c in enumerate(s):
            #seen
            if c in seen:
                #print(f"at {i} found dupe '{c}'")
                if seen[c] >= start:
                    #print(f"hit '{c}' at {i} updating start to {i}")
                    longest = max(longest, i - start)
                    start = seen[c]+1
            #not seen

            seen[c] = i

        print(seen)
        longest = max(longest, len(s)-start)
        return longest