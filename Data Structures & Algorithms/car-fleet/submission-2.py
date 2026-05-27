class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size = len(position)
        combined = [(0,0)] * size #position, time to arrive if no fleeting

        for i in range(size):
            combined[i] = (position[i], (target - position[i]) / speed[i]) # calculate time to arrive

        combined.sort()

        stack = []
        fleets = 0

        for i in range(size-1, -1, -1):
            if len(stack) > 0:
                car = combined[i]
                carInFront = stack[-1]

                if car[1] <= carInFront[1]: #car in front is slower, time to arrive is less
                    combined[i] = (car[0], car[1])
                    continue # it joins the fleet in front, not a new fleet, dont execute rest of loop

            fleets += 1
            stack.append(combined[i])
        
        return fleets
        


            