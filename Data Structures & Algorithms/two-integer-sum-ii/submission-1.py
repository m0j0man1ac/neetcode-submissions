class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1

        while i<j:
            ni = numbers[i]
            nj = numbers[j]
            
            x = target - ni

            while nj > x:
                j -= 1
                nj = numbers[j]
            
            if nj == x and not ni == nj:
                return [i+1, j+1]

            x = target - nj

            while ni < x:
                i += 1
                ni = numbers[i]

            if ni == x and not ni == nj:
                return [i+1, j+1]

        return []