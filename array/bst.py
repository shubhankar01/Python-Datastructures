class Bst:
    def __init__(self, data = None):
        self.data = data
        if self.data:
            self.left = Bst()
            self.right = Bst()
        else:
            self.left = None
            self.right = None

    def insert(self,data):
        if self.data is None:
            self.data = data
            self.left = Bst()
            self.right = Bst()
        elif self.data > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                temp = Bst(data)
                self.left = temp
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                temp = Bst(data)
                self.right = temp

    def inorder(self):
        if self.data is None:
            return
        else:
            self.left.inorder()
            print(self.data)
            self.right.inorder()

    def insert_queue(self,queue):
        if self.left.data:
            queue.append(self.left)
        if self.right.data:
            queue.append(self.right)

    def levelorder(self):
        if self.data is None:
            return
        else:
            print(self.data)
            queue = []
            self.insert_queue(queue)
            while queue:
                print(queue[0].data)
                queue[0].insert_queue(queue)
                del queue[0]

    def printleaf(self):
        if self.data is None:
            return
        else:
            if self.left.data is None and self.right.data is None:
                print(self.data)
            self.left.printleaf()
            self.right.printleaf()

    def printleftnodes(self):
        if self.data is None:
            return
        else:
            print(self.data)
            self.left.printleaf()

    def printrightnodes(self):
        if self.data is None:
            return
        else:
            print(self.data)
            self.right.printleaf()

    def printedges(self):
        print(self.data)
        self.left.printleftnodes()
        self.right.printrightnodes()

    def height(self):
        if self.data is None:
            return 0
        else:
            return (max(self.left.height()+1, self.right.height()+1))


