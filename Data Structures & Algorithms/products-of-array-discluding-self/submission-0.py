class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProd = [nums[0]]

        for i in range(1, len(nums)):
            prefixProd.append(nums[i] * prefixProd[i-1])

        suffixProd = [0] * len(nums)
        suffixProd[len(nums)-1] = nums[len(nums)-1]

        for i in range(len(nums)-2, -1, -1):
            suffixProd[i] = nums[i] * suffixProd[i+1]

        print(nums)
        print(prefixProd)
        print(suffixProd)

        result = [0] * len(nums)

        for i in range(len(nums)):
            a = 1 if i-1 < 0 else prefixProd[i-1]
            b = 1 if i+1 >= len(nums) else suffixProd[i+1]
            result[i] = a * b

        #print(result)
        return result

