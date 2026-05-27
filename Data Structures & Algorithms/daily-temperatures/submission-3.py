class Solution:
    #dynamic programming solution from hints
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        size = len(t)

        results = [0] * size

        for i in range(size-2, -1, -1):
            j = i+1
            while(j<size):
                if t[j] > t[i]:
                    results[i] = j - i
                    break
                
                j = j + max(1, results[j])

        return results