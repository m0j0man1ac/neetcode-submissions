class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences: Dict[int, int] = {}

        for n in nums:
            if n not in occurences:
                occurences[n] = 1
            else:
                occurences[n] += 1

        sorted_nums = sorted(occurences.items(), key=lambda item: item[1], reverse=True)
        
        answer = []

        for i, n in enumerate(sorted_nums):
            if i >= k:
                break
            
            answer.append(n[0])  

        return answer