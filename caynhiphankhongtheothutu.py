# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root): # duyệt cây LNR
        if root==None: return []
        l=[]
        l+=self.inorderTraversal(root.left)
        l.append(root.val)
        l+=self.inorderTraversal(root.right)
        return l

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        