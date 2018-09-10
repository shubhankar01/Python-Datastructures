INT_MAX = 4294967296
INT_MIN = -4294967296


def isBST(root):
    # Code here
    # return 1
    return check_bst(root, INT_MIN, INT_MAX)


def check_bst(root, mi, mx):
    if root is None:
        return True
    else:
        if root.data < mi or root.data > mx:
            return False
        return (check_bst(root.left, mi, root.data - 1) and check_bst(root.right, root.data + 1, mx))