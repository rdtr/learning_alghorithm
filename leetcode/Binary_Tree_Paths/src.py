# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchTree(self, root, path, allPaths):
        if path == "":
            path += str(root.val)
        else:
            path += "->" + str(root.val)
        
        if not root.left and not root.right:
            allPaths.append(path)
        
        if root.left:
            self.searchTree(root.left, path, allPaths)
        if root.right:
            self.searchTree(root.right, path, allPaths)
    
    def binaryTreePaths(self, root):
        """
            :type root: TreeNode
            :rtype: List[str]
            """
        allPaths = []
        path = ""
        
        if not root:
            return allPaths
        
        self.searchTree(root, path, allPaths)
        return allPaths
