class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @return bool布尔型
#
class Solution:
    pre = None
    def isValidBST(self , root: TreeNode) -> bool:
        if root == None:
            return True
        left = self.isValidBST(root.left) # 左子树是否为二叉搜索树
        if not left:
            return False
        if not self.pre:
            self.pre = root
            temp = True
        else:
            temp = self.pre.val < root.val # 当前节点是否满足二叉搜索树特点
            self.pre = root
        right = self.isValidBST(root.right) # 右子树是否为二叉搜索树
        return left and temp and right # 满足以上3个条件
    