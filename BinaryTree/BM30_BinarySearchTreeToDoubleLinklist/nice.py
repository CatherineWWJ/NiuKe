class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param pRootOfTree TreeNode类
# @return TreeNode类
#
class Solution:
    head = None
    pre = None
    def conV(self, root: TreeNode): # 中序遍历
        if not root:
            return None
        self.conV(root.left)
        if not self.pre: # 标记链头
            self.pre = root
            self.head = root
        else:
            self.pre.right = root
            root.left = self.pre
            self.pre = root # 标记链尾
        self.conV(root.right)

    def Convert(self , pRootOfTree ):
        self.conV(pRootOfTree)
        return self.head
