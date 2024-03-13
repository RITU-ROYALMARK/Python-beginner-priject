# CONSTRUCT A BINARY SEARCH TREE AND INSERT VALUES

class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return

        if self.key == data:
            return

        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = node(data)

        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = node(data)

tree = node(10)
l = [2,3,4,20,30,40,50,1,5,6,7]
for i in l:
    tree.insert(i)

