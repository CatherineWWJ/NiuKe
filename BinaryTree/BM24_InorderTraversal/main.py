class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def inorder(self, root: TreeNode, res: List[int]):
        if root == None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def inorderTraversal(self , root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return res
        self.inorder(root, res)
        return res