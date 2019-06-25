# https://leetcode.com/problems/validate-binary-search-tree/
# https://leetcode.com/articles/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# runtime 44ms, 28%, memory 16.5 MB, 56%
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def traverse(node, lower=float('-inf'), upper=float('inf')):
            if node:
                if node.val <= lower or node.val >= upper:
                    return False
                if not traverse(node.left, lower, node.val):
                    return False
                if not traverse(node.right, node.val, upper):
                    return False
            return True

        return traverse(root)


# test cases:
# [1,1]   returns False
# [10,5,15,null,null,6,20]   returns False
# [2,1,3]   returns True
