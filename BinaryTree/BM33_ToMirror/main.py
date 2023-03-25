class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def toMirror(self, root: TreeNode):
        if root.left == None and root.right == None: # 注意：if-else结构一定要规则！否则递归回来的结果会进入下一个if
            return
        elif root.left != None and root.right == None:
            root.right = root.left
            root.left = None
            self.toMirror(root.right)
        elif root.left == None and root.right != None:
            root.left = root.right
            root.right = None
            self.toMirror(root.left)
        else:
            temp = root.right
            root.right = root.left
            root.left = temp
            self.toMirror(root.left)
            self.toMirror(root.right)

    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        if pRoot == None:
            return pRoot
        self.toMirror(pRoot)
        return pRoot
