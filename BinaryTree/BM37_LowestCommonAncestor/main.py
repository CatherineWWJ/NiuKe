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
class Solution:
    def lowestCommonAncestor(self , root: TreeNode, p: int, q: int) -> int:
        l_path = []
        r_path = []
        cur = root
        while cur.val != p: # 搜索路径
            l_path.append(cur.val)
            if cur.val < p:
                cur = cur.right
            else:
                cur = cur.left
        l_path.append(cur.val)
        cur = root
        while cur.val != q:
            r_path.append(cur.val)
            if cur.val < q:
                cur = cur.right
            else:
                cur = cur.left
        r_path.append(cur.val)
        i,j = 0,0
        while i<len(l_path) and j<len(r_path) and l_path[i] == r_path[j]: # 辅助数组比较
            i += 1
            j += 1
        return l_path[i-1]
