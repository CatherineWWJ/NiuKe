class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param pRoot TreeNode类
# @return bool布尔型
#
class Solution:
    def isSym(self, lRoot: TreeNode, rRoot: TreeNode) -> bool: # 递归地比较2个子树是否对称
        if lRoot == None and rRoot == None:
            return True
        if lRoot == None and rRoot != None:
            return False
        if lRoot != None and rRoot == None:
            return False
        tag1 = lRoot.val == rRoot.val
        tag2 = self.isSym(lRoot.left, rRoot.right)
        tag3 = self.isSym(lRoot.right, rRoot.left)
        return tag1 and tag2 and tag3

    def isSymmetrical(self, pRoot: TreeNode) -> bool:
        if pRoot == None:
            return True
        if pRoot.left == None and pRoot.right == None:
            return True
        return self.isSym(pRoot.left, pRoot.right)

