class TimeMap:
    d : dict[str, list[tuple[int, str]]] = {}

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((timestamp, value))
        else:
            self.d[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        li = self.d[key]
        print(f"get {timestamp}")
        print(li)
        l,r = 0, len(li)-1
        
        last = ""
        while l <= r:
            mid = l + (r-l)//2
            t = li[mid][0]

            if t <= timestamp:
                last = li[mid][1]

            if timestamp == t:
                return last
            elif t <= timestamp:
                l = mid+1
            else:
                r = mid-1

        return last

        
