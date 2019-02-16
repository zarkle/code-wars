"""Binary search tree class."""


from tree_node import Node


class BinarySearchTree:
    """Binary search tree class."""

    def __init__(self):
        """Constructor."""
        self.root = None
        self.size = 0

    def length(self):
        """Return size of tree."""
        return self.size

    def __len__(self):
        """Allows use of the len() built-in method."""
        return self.size

    def __iter__(self):
        """Iterate through the binary search tree, called on root."""
        return self.root.__iter__()

    def insert(self, key, value):
        """Insert a new node into tree."""
        if self.root:
            self._insert(key, value, self.root)
        else:
            self.root = Node(key, value)
        self.size += 1

    def _insert(self, key, value, currentNode):
        """Insert helper method."""
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._insert(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = Node(key, value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._insert(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = Node(key, value, parent=currentNode)