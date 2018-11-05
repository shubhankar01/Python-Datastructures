def getNthFromLast(head, n):
    # Code here
    li = {}
    temp = head
    count = 1
    while temp is not None:
        li[count] = temp.data
        temp =  temp.next
        count+=1
    if count < n:
        return -1
    else:
        return li[count-n]