# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        fast, slow = prev, head

        while slow and fast:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True

