class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param pRootOfTree TreeNode类
# @return TreeNode类
#
class Solution:
    def conV(self, root: TreeNode, res: List[TreeNode]): # 中序遍历
        if not root:
            return
        self.conV(root.left, res)
        res.append(root)
        self.conV(root.right, res)

    def Convert(self , pRootOfTree ):
        if pRootOfTree == None:
            return pRootOfTree
        res = []
        self.conV(pRootOfTree, res)
        for i in range(len(res)-1): # 构建链表
            res[i].right = res[i+1]
        for i in range(1, len(res)):
            res[i].left = res[i-1]
        return res[0]
    