# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        i,j = list1,list2
        while i and j:
            if i.val <= j.val:
                temp.next = ListNode(i.val)
                i = i.next
                temp = temp.next
            else:
                temp.next = ListNode(j.val)
                j = j.next
                temp = temp.next
        
        while i:
            temp.next = ListNode(i.val)
            i = i.next
            temp = temp.next
        while j:
            temp.next = ListNode(j.val)
            j = j.next
            temp = temp.next
        return dummy.next
