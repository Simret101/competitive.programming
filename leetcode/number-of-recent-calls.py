class RecentCounter:

    def __init__(self):
        self.q=deque()
        self.length=0
        

    def ping(self, t: int) -> int:
        self.length=0
        self.q.append(t)
        r=deque(self.q)
        while r:
            n=r.pop()
            if n<(t-3000):
                return self.length
            else:
                self.length+=1
        
        return self.length
        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)