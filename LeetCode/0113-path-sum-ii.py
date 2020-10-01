from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root, key, stack, res):
        if root:
            stack.append(root.val)
            key = key - root.val
            if(key == 0 and root.left == None and root.right == None):
                res += [list(stack)]
            self.preorder(root.left, key, stack, res)
            self.preorder(root.right, key, stack, res)
            key += stack.pop()
            
    def pathSum(self, root: TreeNode, key: int) -> List[List[int]]:
        res = []
        stack = []
        self.preorder(root, key, stack, res)
        # print(res)
        return res
        