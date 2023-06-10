# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        dummy = ListNode(0)
        dummy.next = head
        while cur:
            l += 1
            cur = cur.next

        cur, x = dummy, 0
        while x != l-n:
            cur = cur.next
            x += 1
        cur.next = cur.next.next
        return dummy.next

        

