# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        prev=None
        cur=head
        ans=[]
        n=0
        while cur:
            n+=1
            cur=cur.next
        print(n)
        length=n//k
        remain=n%k
        cur=head
        for _ in  range(k):
            ans.append(cur)
            for _ in range(length):
                if cur:
                    prev=cur
                    cur=cur.next
            if remain and cur:
                prev=cur
                cur=cur.next
                remain-=1
            if prev:
                prev.next=None
                    
           
        return ans
        
            