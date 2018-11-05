def size(node):
    # code here
    if node == None:
        return 0
    else:
        return ((size(node.left) + size(node.right))+1)