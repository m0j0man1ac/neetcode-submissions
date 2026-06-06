class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        
        rowi = -1
        while l<=r:
            mid = l + (r-l)//2
            nl = matrix[mid][0]
            nr = matrix[mid][len(matrix[mid])-1]

            #target smaller
            if target < nl:
                r = mid-1
            #target bigger
            elif target > nr:
                l = mid+1
            #found row
            else:
                rowi=mid
                break
        
        if rowi == -1:
            return False

        row = matrix[rowi]
        l,r = 0, len(row)-1

        while l<=r:
            mid = l + (r-l)//2
            n = row[mid]

            #target smaller
            if target < n:
                r = mid-1
            #target bigger
            elif target > n:
                l = mid+1
            #found target
            else:
                return True

        return False

        

                

        