"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dic = defaultdict(Node)
        cur = head
        dummy = Node(0)
        temp = dummy
        while cur:
            if cur in dic:
                temp.next = dic[cur]
            else:
                neww = Node(cur.val)
                temp.next = neww
                dic[cur] = neww
            if not cur.random:
                temp.next.random = None
            elif cur.random in dic:
                temp.next.random = dic[cur.random]
            else:
                neww = Node(cur.random.val)
                temp.next.random = neww
                dic[cur.random] = neww
            
            temp = temp.next
            cur = cur.next
        return dummy.next



