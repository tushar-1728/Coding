# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calc_diameter(self, diameter, node):
        if node:
            l_height = calc_diameter(node.left)
            r_height = calc_diameter(node.right)
            diameter[0] = max(diameter[0], l_height + r_height + 1)
            return 1 + max(l_height, r_height)
        return 0


    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root:
            diameter = [-1]
            calc_diameter(diameter, root)
            return diameter[0] - 1
        return 0


# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]