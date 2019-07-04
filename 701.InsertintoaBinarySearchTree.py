# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        temp = root
        while True:
            if temp.val < val and temp.right:
                temp = temp.right
            elif temp.val < val and temp.right==None:
                temp.right = TreeNode(val)
                return root
            elif temp.val > val and temp.left:
                temp = temp.left
            else:
                temp.left = TreeNode(val)
                return root
