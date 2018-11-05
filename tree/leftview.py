def printLeftView(root):
    # Code here
    a = [root, 'L']
    print(root.data)
    while a:
        temp = a[0]
        del(a[0])
        if temp == 'L':
            if a:
                print(a[0].data)
                a.append(temp)
            else:
                break
        else:
            if temp.left:
                a.append(temp.left)
            if temp.right:
                a.append(temp.right)