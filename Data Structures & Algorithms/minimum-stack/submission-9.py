class MinStack: #encoded stack, tracks difference from current min
    l = None
    m = None

    def __init__(self):
        self.l = []

    def push(self, val: int) -> None:
        if len(self.l) == 0:
            self.m = val
            self.l.append(0)
        elif val < self.m:
            self.l.append(val - self.m)
            self.m = val
        else:
            self.l.append(val-self.m)

        print(f"push {val}: min {self.m} encode {self.l[-1]}")

    def pop(self) -> None:
        val = self.l[-1]
        n = self.m + val

        if val < 0:
            self.m -= val

        self.l.pop()

        if len(self.l) == 0:
            self.m == None
        

    def top(self) -> int:
        print(self.m)
        val = self.l[-1]
        if val <= 0:
            return self.m
        return val+self.m
        

    def getMin(self) -> int:
        return self.m
        
