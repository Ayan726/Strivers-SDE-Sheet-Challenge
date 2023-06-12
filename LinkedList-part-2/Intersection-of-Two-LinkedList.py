# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        it1, it2 = headA, headB

        while it1 != it2:
            it1 = it1.next if it1 else headB
            it2 = it2.next if it2 else headA
        
        return it1
