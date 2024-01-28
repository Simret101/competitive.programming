# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast.next  and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        revHead = self.reverse(slow)
        while revHead :
            if revHead.val != head.val:
                return False
            else:
                revHead = revHead.next
                head = head.next
        return True

    def reverse(self, head):
        prev = None
        while head :
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev