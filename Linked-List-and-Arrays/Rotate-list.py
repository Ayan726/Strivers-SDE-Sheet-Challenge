# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l = 0
        cur = head
        prev = cur
        while cur:
            l += 1
            prev = cur
            cur = cur.next
        k %= l
        if not k:
            return head
        l -= k
        cur = head
        while cur and l != 1:
            cur = cur.next
            l -= 1
        prev.next = head
        res = cur.next
        cur.next = None
        return res
