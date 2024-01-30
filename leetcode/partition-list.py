# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummyMin = ListNode(0)
        dummyMax = ListNode(0)
        minNode = dummyMin
        maxNode = dummyMax
        while head:
            if head.val < x:
                minNode.next = head
                minNode = minNode.next
            else:
                maxNode.next = head
                maxNode = maxNode.next
            head = head.next
        minNode.next = dummyMax.next
        maxNode.next = None
        return dummyMin.next