# Given a singly linked list, find middle of the linked list. For example,
# if given linked list is 1->2->3->4->5 then output should be 3.
# If there are even nodes, then there would be two middle nodes, we need to print
# second middle element. For example, if given linked list is 1->2->3->4->5->6 then output should be 4.


def find_mid(head):
    # Code here
    count = 0
    arr = {}
    if head is None:
        return -1
    while head:
        count +=1
        arr[count] = head
        head = head.next
    index = (count//2)+1
    return arr[index]
