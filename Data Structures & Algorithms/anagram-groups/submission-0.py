class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occurenceList = []
        
        # turn the list of strings into a list of 26 len arrays which count occurences of char by alphabetical order
        for i, s in enumerate(strs):
            lowerS = s.lower()
            curOccurences = [0] * 26

            for c in s:
                curOccurences[ord(c) - ord('a')] += 1

            occurenceList.append(tuple(curOccurences))


        
        #sorted anagram hashset
        #key is occurences, values are a list of idx
        sortedAna = defaultdict(list)

        # use i to keep track of orignal string index
        for i, l in enumerate(occurenceList):
            if l not in sortedAna:
                sortedAna[l] = [strs[i]]
            else:
                sortedAna[l].append(strs[i])

        # print(sortedAna)

        return list(sortedAna.values())

        