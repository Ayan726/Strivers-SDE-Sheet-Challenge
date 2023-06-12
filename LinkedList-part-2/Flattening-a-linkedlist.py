def flatten(root):
    if not root or not root.next:
        return root
    cur = root.next 
    while cur:
        nex = cur.next
        temp = cur
        while temp:
            x = temp.data
            b = temp.bottom
            a, prev = root, None
            while a and a.data<=x:
                prev = a
                a = a.bottom
            nxt = prev.bottom
            prev.bottom = temp
            temp.bottom = nxt
            temp = b

        cur = nex
    
    return root
