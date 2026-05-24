class Solution:
    #O(n^2) using two points
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #a+b+c=0
        #a<=b<=c
        #a<=0
        res = []

        #sort to allow the 2 pointer approach
        nums.sort()

        for i, a in enumerate(nums):
            #no longer any more possible triplets based on constraints
            if a>0:
                break

            #skip dupes for a
            if i>0 and a == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1

            #loop to search for triplet 0 sum
            while j<k:
                tsum = a + nums[j] + nums[k]

                #increase/decrease a or b respectively based on current sum
                if tsum > 0:
                    k -= 1
                elif tsum < 0:
                    j += 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j+=1
                    k-=1
                    #mini inner dupe check for b
                    while nums[j] == nums[j-1] and j<k:
                        j+=1

        return res

