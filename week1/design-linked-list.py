class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
      
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len=0
        
    def get(self, index: int) -> int:
        if index >= self.len:
            return -1

        cur=self.head
        for i in range(index):
            
            cur=cur.next

        return cur.val
        
    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next=self.head
        self.head = newnode
        self.len+=1
      
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return

        cur=self.head
        while cur and cur.next:
            cur=cur.next
        newnode=Node(val)
        cur.next=newnode
        self.len+=1

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return

        if self.len>=index:
            newnode=Node(val)
            cur=self.head

            for i in range(index-1):
                
                cur= cur.next
            
        
            newnode.next=cur.next
            cur.next=newnode
            self.len+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if self.len>index:

            if index==0:
                self.head=self.head.next
                self.len -= 1
                return

            cur=self.head

            for i in range(index-1):
                
                cur= cur.next
            cur.next=cur.next.next
            self.len-=1
       
   


        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)