class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def traverse(self, root: TreeNode, res: List[int]):
        if root.left:
            self.traverse(root.left, res)
        if root.right:
            self.traverse(root.right, res)
        res.append(root.val)

    def postorderTraversal(self , root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return res
        self.traverse(root, res)
        return res