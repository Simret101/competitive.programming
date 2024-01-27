# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur=head
        # while cur and cur.next:  
        #     x=cur.next.next
        #     cur.next=cur
        #     cur=cur.next
        # if head:
        #     head.next=None
        prev=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            
        return prev



      