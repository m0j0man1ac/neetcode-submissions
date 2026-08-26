class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        tMap : dict[str, int] = {}
        matches = 0

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        sMap : dict[str, int] = {}

        found = False
        shortL = len(s)
        shortIdx : tuple[int, int] = (0,0)

        l,r = 0,0
        while r < len(s):
            rc = s[r]
            if rc in tMap:
                sMap[rc] = sMap.get(rc, 0) + 1
                if tMap[rc] == sMap[rc]:
                    matches += 1

            #matches found
            #try update answer
            #try trim from left
            while matches >= len(tMap) and l<=r:
                found = True
                if shortL > r-l:
                    shortL = r-l
                    shortIdx = (l,r)
                
                #if l<r:
                lc = s[l]
                if lc in tMap:
                    sMap[lc] = sMap.get(lc, 0) - 1
                    if sMap[lc] == tMap[lc] - 1:
                        matches -= 1
                
                l += 1

            r += 1

        if found:
            return s[shortIdx[0] : shortIdx[1]+1]

        return ""


