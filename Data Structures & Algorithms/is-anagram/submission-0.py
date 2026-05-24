class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sOccurences: dict[str, int] = {}
        tOccurences: dict[str, int] = {}

        for i in range(len(s)):
            Solution.AddOrIncrementEntryInSet(s[i], sOccurences)
            Solution.AddOrIncrementEntryInSet(t[i], tOccurences)

        """
        for key in sOccurences:
            if key not in tOccurences or sOccurences[key] != tOccurences[key]:
                return False

        return True
        """

        return sOccurences == tOccurences


    @staticmethod
    def AddOrIncrementEntryInSet(x: str, curDict: dict[str, int]):
        if x not in curDict:
            curDict[x] = 1
        else:
            curDict[x] += 1
