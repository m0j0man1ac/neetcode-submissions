class MinStack:
    l = None
    minl = None

    def __init__(self):
        self.l = []
        self.minl = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if not self.minl or val <= self.minl[-1]:
            self.minl.append(val)


    def pop(self) -> None:
        if self.l[-1] == self.minl[-1]:
            self.minl.pop()
        self.l.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.minl[-1]
        
