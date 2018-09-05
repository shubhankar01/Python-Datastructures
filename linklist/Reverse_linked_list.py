def reverseList(self):
    # Code here
    if self.head is None:
        return None
    prev = None
    current = self.head
    while current is not None:
        n = current.next
        current.next = prev
        prev = current
        current = n
    self.head = prev
    return self.head
