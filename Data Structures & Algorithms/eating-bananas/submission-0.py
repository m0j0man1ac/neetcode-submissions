class Solution:
    import math

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        size = len(piles)
        

        lPile = -1
        for i,n in enumerate(piles):
            lPile = max(lPile, n)
        
        print(f"largest pile {lPile}")
        lastK = lPile

        l,r = 1, lPile

        while l<=r:
            mid = l + (r-l)//2
            print(f"mid {mid}")

            sumC = 0

            for i,n in enumerate(piles):
                sumC += (n+mid-1)//mid

            print(f"sumC {sumC}")

            if sumC <= h:
                lastK = min(mid, lastK)

            #not fast enough, need faster eat speed
            if sumC > h:
                l = mid + 1
            #potentially more time, can have slower speed, smaller mid
            else:
                r = mid - 1
            


        return lastK
