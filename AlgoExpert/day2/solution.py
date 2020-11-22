# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        parent_node = node
        while node is not None:
            parent_node = node
            if value >= node.value:
                node = node.right
            else:
                node = node.left
        new_node = BST(value)
        if parent_node.value > value:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        return self

    def contains(self, value):
        # Write your code here.
        node = self
        while node:
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            else:
                node = node.right
        return False


    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        """
        cases:
        1. remove leaf node
        2. remove node with just one child
        3. remove a node with both left and right children
        """
        if not self.contains(value):
            return self
        node = self
        parent_node = self
        while node.value != value:
            parent_node = node
            if node.value > value:
                node = node.left
            else:
                node = node.right
        if node.left is None and node.right is None:
            if parent_node.left == node:
                parent_node.left = None
            else:
                parent_node.right = None

        elif node.left is not None and node.right is not None:
            nnode = self._get_leftmost_node(node.right)
            node.value = nnode.value
        else:
            if node.left is None:
                if parent_node.left == node:
                    parent_node.left = node.right
                else:
                    parent_node.right = node.right
            else:
                if parent_node.left == node:
                    parent_node.left = node.left
                else:
                    parent_node.right = node.left
        return self

    def _get_leftmost_node(self, node):
        parent_node = node
        while node.left is not None:
            parent_node = node
            node = node.left
        parent_node.left = None
        return node
