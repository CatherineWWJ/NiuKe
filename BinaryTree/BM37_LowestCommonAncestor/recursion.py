class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @param p int整型
# @param q int整型
# @return int整型
#
# 思路：
# 利用二叉搜索树的性质：
# 1.对于某一个节点若是p与q都小于等于这个这个节点值，说明p、q都在这个节点的左子树，而最近的公共祖先也一定在这个节点的左子树；
# 2.若是p与q都大于等于这个节点，说明p、q都在这个节点的右子树，而最近的公共祖先也一定在这个节点的右子树。
# 3.而若是对于某个节点，p与q的值一个大于等于节点值，一个小于等于节点值，说明它们分布在该节点的两边，而这个节点就是最近的公共祖先
class Solution:
    def findCommon(self, root: TreeNode, p: int, q: int) -> int:
        if p<=root.val<=q:
            return root.val
        elif root.val>p and root.val>q: # p,q的最近公共祖先在root的左子树
            return self.findCommon(root.left, p, q)
        else: # p,q的最近公共祖先在root的右子树
            return self.findCommon(root.right, p, q)

    def lowestCommonAncestor(self , root: TreeNode, p: int, q: int) -> int:
        if p>q:
            return self.findCommon(root, q, p)
        else:
            return self.findCommon(root, p, q)
