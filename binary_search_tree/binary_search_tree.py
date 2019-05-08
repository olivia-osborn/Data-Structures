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
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
