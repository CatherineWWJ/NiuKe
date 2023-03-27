class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , pre: List[int], vin: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        top = vin.index(pre[0])
        left = self.reConstructBinaryTree(pre[1:1+top], vin[0:top])
        right = self.reConstructBinaryTree(pre[1+top:], vin[top+1:])
        root.left = left
        root.right = right
        return root
