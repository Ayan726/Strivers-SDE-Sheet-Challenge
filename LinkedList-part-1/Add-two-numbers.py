# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 is not None or l2 is not None or carry:
            total_sum = 0
            
            if l1 is not None:
                total_sum += l1.val
                l1 = l1.next
            
            if l2 is not None:
                total_sum += l2.val
                l2 = l2.next
            
            total_sum += carry
            carry = total_sum // 10
            
            curr.next = ListNode(total_sum % 10)
            curr = curr.next
        
        return dummy.next
