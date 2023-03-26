class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def Mirror(self, pRoot: TreeNode) -> TreeNode: # 自底向上：后序递归
        # 空树返回
        if not pRoot:
            return None
        # 先递归子树
        left = self.Mirror(pRoot.left)
        right = self.Mirror(pRoot.right)
        # 交换
        pRoot.left = right
        pRoot.right = left
        return pRoot
