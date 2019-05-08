# right side is smaller
# left side is bigger


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # check if new node's value is less than the current node's value:
        if value < self.value:
            # check if no left child:
            if not self.left:
                # set new node here:
                self.left = BinarySearchTree(value)
            # otherwise, keep traversing:
            else:
                self.left.insert(value)
        # do the same on the right side:
        else:
            # check if no right child:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # result = False
        if target == self.value:
            return True
        elif target < self.value:
            # check if no left child:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        # check if self.value has no right child:
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        pass

    def __str__(self):
        return f'value: {self.value}, left: {self.left}, right: {self.right}: max: {self.get_max()}'


bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(12)
bst.insert(19)
bst.insert(11)
bst.insert(55)
# bst.get_max()
print(bst)
