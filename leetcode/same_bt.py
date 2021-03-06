# https://leetcode.com/problems/same-tree/description/
# https://leetcode.com/articles/same-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 36ms, 89%
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p and not q) or (q and not p):
            return False
        if not p and not q:
            return True

        queue1 = [p]
        queue2 = [q]

        while queue1:
            curr1 = queue1.pop(0)
            curr2 = queue2.pop(0)
            if curr1.val != curr2.val:
                return False
            if curr1.left and curr2.left:
                queue1.append(curr1.left)
                queue2.append(curr2.left)
            elif (curr1.left and not curr2.left) or (curr2.left and not curr1.left):
                return False
            if curr1.right and curr2.right:
                queue1.append(curr1.right)
                queue2.append(curr2.right)
            elif (curr1.right and not curr2.right) or (curr2.right and not curr1.right):
                return False
        return True


# test cases:
# [] []
# [1,2] [1, null, 2]
# [1] []
# [2,null,4] [2,3,4]

# How to think about this for a 1-line solution:
# The example submission for the 100% C solution is about 30 lines. Yikes. Think more, code less. Only one line is needed.
# If tree p is empty, then return true if and only if q is empty. Otherwise p is not empty, so return true if and only if q is also not empty, its root value matches the root value of q, and both left and right subtrees match.
# Now both of these alternatives return, so we can put both branches in a ternary expression and return its value instead:

# bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
#   return !p ? !q : q && p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
# }


# another shorter python solution:
def isSameTree(self, p, q):
    stack = []
    stack.append((p,q))
    while stack:
        p, q = stack.pop()
        if not p and not q:
            continue

	if p and q:
	    if p.val != q.val:
		return False
	    else:
	        stack.append((p.left, q.left))
	        stack.append((p.right, q.right))
	else:
	    return False

    return True



class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p or not q:
            if not p and not q:
                return True
            return False

        qp = [p]
        qq = [q]

        while qp:
            currp = qp.pop(0)
            currq = qq.pop(0)

            if currp.val != currq.val:
                return False

            if currp.left and currq.left:
                qp.append(currp.left)
                qq.append(currq.left)
            elif (currp.left and not currq.left) or (currq.left and not currp.left):
                return False
            if currp.right and currq.right:
                qp.append(currp.right)
                qq.append(currq.right)
            elif (currp.right and not currq.right) or (currq.right and not currp.right):
                return False

        return True


# 36 ms, 89%
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False

        queueP = [p]
        queueQ = [q]

        while queueP and queueQ:
            currP = queueP.pop(0)
            currQ = queueQ.pop(0)
            if currP.val != currQ.val or \
                (currP.left and not currQ.left) or \
                (currQ.left and not currP.left) or \
                (currP.right and not currQ.right) or \
                (currQ.right and not currP.right):
                return False
            if currP.left and currQ.left:
                queueP.append(currP.left)
                queueQ.append(currQ.left)
            if currP.right and currQ.right:
                queueP.append(currP.right)
                queueQ.append(currQ.right)
        if currP.left or currP.right or currQ.left or currQ.right:
            return False

        return True


# 32 ms, 100%
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return p == q


# 40 ms, 50%
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Pathrise solution
# runtime 16 ms, 75%; memory 11.9 MB, 23%
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Base case
        if not p and not q: return True
        if not p or not q: return False

        # Request
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        # Return
        return left is True and right is True and p.val == q.val


# Pathrise solution with early exit, doing processing earlier [supposed to be faster]
# runtime 20 ms, 43%; memory 11.9 MB, 18%
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Base case
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val:
            return False

        # Request
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        # Return
        return left is True and right is True
