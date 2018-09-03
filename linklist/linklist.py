class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def append(self, data):
        if self.data is None:
            self.data = data
        elif self.next is None:
            print('hi')
            temp = Node(data)
            self.next = temp
        else:
            self.next.append(data)

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            temp = Node(data)
            temp.data, self.data = self.data, temp.data
            self.next, temp.next = temp, self.next

    def delete(self, data):
        if self.data == data:
            if self.next == None:
                self.data = None
            else:
                self.value = self.next.value
                self.next = self.next.next
        else:
            temp = self.next
            temp2 = self
            while temp != Node and temp.data != data :
                temp = temp.next
                temp2 = temp2.next
            temp2.next = temp.next