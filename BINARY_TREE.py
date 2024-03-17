# BINARY SEARCH TREE

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data == data:
            return

        if self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = TreeNode(data)

    def search(self, val):
        if self.data == val:
            return val

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order(self):
        elements = []

        if self.left:
            elements += self.left.in_order()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()
        return elements

    def pre_order(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order()

        if self.right:
            elements += self.right.pre_order()

        return elements

    def post_order(self):
        elements = []

        if self.left:
            elements += self.left.post_order()

        if self.right:
            elements += self.right.post_order()

        elements.append(self.data)

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.right is None:
            return self.data
        return self.right.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    root = TreeNode(elements[0])
    for i in range(1, len(elements)):
        root.insert(elements[i])

    return root


num = [2, 3, 4, 6, 7, 8, 9, 10, 20, 59, 34, 56]

number = build_tree(num)
print("Min:", number.find_min())
print("Max:", number.find_max())
print("Sum:", number.calculate_sum())
print(f"SEARCH THE VALUE: {number.search(3)}")
print(f"THE IN_ORDER: {number.in_order()}")
print(f"THE PRE_ORDER: {number.pre_order()}")
print(f"THE POST_ORDER: {number.post_order()}")













































































































































