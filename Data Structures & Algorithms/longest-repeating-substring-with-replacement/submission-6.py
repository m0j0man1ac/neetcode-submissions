class Solution:
    #optimal sliding window solution given by neetcode
    #coded from instructions, not copy paste
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0

        counts : dict[str, int] = {}
        maxFreq = 0
        res = 0
        l = 0

        for i, c in enumerate(s):
            counts[c] = counts.get(c, 0) + 1
            maxFreq = max(maxFreq, counts[c])

            windowSize = (i - l + 1)

            if windowSize - maxFreq > k:
                lChar = s[l]
                counts[lChar] = counts.get(lChar, 0) - 1
                l += 1
            else:
                res = max(res, windowSize)

        return res