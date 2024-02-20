class Node:
    def __init__(self,val, prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.temp= Node(homepage)
        

    def visit(self, url: str) -> None:
        self.temp.next=Node(url,self.temp)
        self.temp=self.temp.next
        

    def back(self, steps: int) -> str:
        while steps>0 and self.temp.prev:
            

            self.temp=self.temp.prev
            steps-=1
        return self.temp.val
        

    def forward(self, steps: int) -> str:
        while steps>0 and self.temp.next:
           
            self.temp=self.temp.next
            steps-=1
        return self.temp.val

       


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)              