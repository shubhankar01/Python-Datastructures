def rotateList(head, k):
    # code here
    c = head
    n = c.next
    while n is not None:
        n = n.next
        c = c.next
    while k:
        temp = head
        c.next = temp
        head = head.next
        temp.next = None
        c = temp
        k-=1
    return head
