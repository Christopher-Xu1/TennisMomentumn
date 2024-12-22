class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None, left_weight=None, right_weight=None):
            self.data = data
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = None

            self.left_weight = left_weight
            self.right_weight = right_weight


    def __init__(self, root=None):
        self.root = root
