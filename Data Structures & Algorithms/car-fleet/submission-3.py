class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target-p)/s for p,s in sorted(zip(position, speed), reverse=True)]

        stack=[]
        for t in time:
            if len(stack) > 0:
                if t <= stack[-1]:
                    continue
            
            stack.append(t)

        return len(stack)