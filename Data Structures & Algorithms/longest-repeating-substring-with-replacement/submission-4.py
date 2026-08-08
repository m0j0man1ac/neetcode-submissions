from dataclasses import dataclass

@dataclass
class CharEntry:
    left : int
    count : int


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0

        res = 1
        charSet = set(s)
        seq : dict[str, CharEntry] = {}
        
        for c in charSet:
            seq[c] = CharEntry(0,0)


        for i, c in enumerate(s):
            #update other non matching entries
            for char, entry in seq.items():
                if char == c:
                    continue

                #if too many gaps
                #reduce move left one and reduce count if that consumed a matching char in window
                while (i - entry.left + 1) - entry.count > k:
                    if s[entry.left] == char:
                        entry.count -= 1
                    entry.left += 1

                res = max(res, i - entry.left + 1)
            
            #c not in dict yet
            if(c not in seq):
                seq[c] = CharEntry(i, 1)
                continue

            #adding to matching dict entry
            seq[c].count += 1

            res = max(res, i - seq[c].left + 1)

        return res 
            