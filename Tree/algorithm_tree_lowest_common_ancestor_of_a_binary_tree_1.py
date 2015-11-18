# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        node_parent = {} # key: node, value: node's parent
        queue = deque([root])
        # traverse all nodes by BST and construct node_parent map
        while queue:
            node = queue.popleft()
            if node.left:
                node_parent[node.left] = node
                queue.append(node.left)
            if node.right:
                node_parent[node.right] = node
                queue.append(node.right)

        # constcurt node existence on paths of p
        # In python, we can use set instead of dictionary
        # because it also takes O(1) to check value existence
        pParents = set()
        current = p
        while current in node_parent:
            pParents.add(current)
            current = node_parent[current]
        else:
            pParents.add(current)

        # find first common node on paths of p and q
        current = q
        while current not in pParents:
            current = node_parent[current]
        return current
        
