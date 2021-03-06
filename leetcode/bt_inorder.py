# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# https://leetcode.com/articles/binary-tree-inorder-traversal


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# (recursive) runtime 20 ms, 100%; memory 10.7 MB, 62%
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        if not root:
            return res

        def travel(node):
            if not node:
                return
            travel(node.left)
            res.append(node.val)
            travel(node.right)

        travel(root)
        return res


# (iterative) runtime 20 ms, 100%; memory 10.9 MB, 6%
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []

        if not root:
            return res

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right

        return res


# runtime 36 ms, 77%; memory 13.1 MB, 6%
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        traverse = []

        def _traverse(node):
            if node:
                if node.left:
                    _traverse(node.left)
                traverse.append(node.val)
                if node.right:
                    _traverse(node.right)

        _traverse(root)
        return traverse


# runtime 36 ms, 77%; memory 13 MB, 6%
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right

        return res
