class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1sorted = sorted(s1)
        s1set = set(s1)

        l = len(s1)

        #s1dict = {}

        #for c in s1:
            #s1dict[c] = s1dict.get(c,0) + 1

        substring = "*" * l

        #for i,c in enumerate(s2):
        for i in range(len(s2)):
            c = s2[i]

            if c in s1set and i+l <= len(s2):
                if sorted(s2[i:i+l]) == s1sorted:
                    return True
                #i += l

        return False
