class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param t1 TreeNode类
# @param t2 TreeNode类
# @return TreeNode类
#
class Solution:
    def mergeT(self, t1: TreeNode, t2: TreeNode):
        if t1.left == None:
            t1.left = t2.left
        else:
            if t2.left != None:
                t1.left.val += t2.left.val
                self.mergeT(t1.left, t2.left)
        if t1.right == None:
            t1.right = t2.right
        else:
            if t2.right != None:
                t1.right.val += t2.right.val
                self.mergeT(t1.right, t2.right)

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val += t2.val
        self.mergeT(t1, t2)
        return t1