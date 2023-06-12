# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        hare, turtle = head, head

        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if hare == turtle:
                return True
        
        return False
            
