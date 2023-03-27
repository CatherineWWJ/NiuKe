class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @return bool布尔型
#
import sys
class Solution:
    pre = -sys.maxsize - 1
    def isValidBST(self , root: TreeNode) -> bool:
        if not root:
            return True
        # 先进入左子树
        if not self.isValidBST(root.left): # 左子树不满足二叉搜索树的特点就直接返回
            return False
        if(root.val <= self.pre): # 同理：当前节点
            return False
        # 更新最值
        self.pre = root.val
        # 再进入右子树
        if not self.isValidBST(root.right): # 同理：右子树
            return False
        return True
