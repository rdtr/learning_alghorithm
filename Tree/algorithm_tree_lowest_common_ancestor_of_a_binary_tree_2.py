# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if not p or not q: return None

        pQueue = []
        self.findPath(root, p, pQueue)
        qQueue = []
        self.findPath(root, q, qQueue)

        common = pQueue[0]
        pLen, qLen = len(pQueue), len(qQueue)
        i = 0

        # iterate from root to P, Q and return the last common node
        while True:
            pRoot = pQueue[i]
            qRoot = qQueue[i]
            if pRoot != qRoot:
                return common
            # when one is a parent of another
            if i == pLen - 1 or i == qLen - 1:
                return pRoot
            common = pRoot
            i += 1

    # returns a path from root as a queue
    def findPath(self, root, node, currentPath):
        if root == node:
            currentPath.append(root.val)
            return True
        if root.left:
            currentPath.append(root.val)
            if self.findPath(root.left, node, currentPath):
                return True
        if root.right:
            currentPath.append(root.val)
            if self.findPath(root.right, node, currentPath):
                return True
        currentPath.pop()
        return False
