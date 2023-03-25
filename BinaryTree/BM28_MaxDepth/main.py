class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @return int整型
#
class Solution:
    def maxD(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l_depth = self.maxD(root.left) + 1
        r_depth = self.maxD(root.right) + 1
        return l_depth if l_depth>=r_depth else r_depth

    def maxDepth(self , root: TreeNode) -> int:
        return self.maxD(root)