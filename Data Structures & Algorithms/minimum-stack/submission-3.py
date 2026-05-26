class MinStack:
    l = None
    minandI = None

    def __init__(self):
        self.l = []

    def push(self, val: int) -> None:
        if not self.minandI or self.minandI[0] > val:
            self.minandI = (val, len(self.l))                
        
        self.l.append(val)

    def pop(self) -> None:
        self.l.pop()

        if self.minandI:
            if self.minandI[1] == len(self.l): #if min was the popped item
                self.minandI = None

                for i, n in enumerate(self.l): #go loop to find a new min :c
                    if not self.minandI or self.minandI[0] > n:
                        self.minandI = (n, i)    

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.minandI[0]
        
