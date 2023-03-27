class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    flag = False
    def dfs(self, root: TreeNode, o: int, path: List[int]):
        if not root:
            return
        path.append(root.val)
        if root.val == o:
            self.flag = True
            return
        self.dfs(root.left, o, path)
        self.dfs(root.right, o, path)
        if self.flag:
            return
        path.pop()

    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        path1 = []
        self.dfs(root, o1, path1)
        path2 = []
        self.flag = False
        self.dfs(root, o2, path2)
        i = 0
        while i<len(path1) and i<len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]
