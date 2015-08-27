# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        res.append([root.val])
        rootQueue = [root]

        while True:
            childrenQueue = []

            while rootQueue:
                parent = rootQueue[0]

                if parent.left:
                    childrenQueue.append(parent.left)
                if parent.right:
                    childrenQueue.append(parent.right)
                rootQueue.pop(0)
                
            if childrenQueue:
                res.append([item.val for item in childrenQueue])
                rootQueue = childrenQueue
            else:
                break
        return res
