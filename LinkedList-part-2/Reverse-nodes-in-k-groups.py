# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l = 0
        cur = head
        res = None
        while cur:
            l += 1
            if l == k:
                res = cur
            cur = cur.next
        
        cur, cnt, prev, nxt = head, 0, None, head
        track = []
        while cur and cnt < l - l%k:
            x = k
            start = nxt
            prev = None
            while cur and x:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                x -= 1
            track.append([start, prev])
            cnt += k
            if cnt == l-l%k:
                track.append([cur,cur])
        
        for i in range(len(track)-1):
            track[i][0].next = track[i+1][1]
        return res




