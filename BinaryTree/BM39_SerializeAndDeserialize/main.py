# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        s = []
        if not root:
            return s
        q = []
        q.append(root)
        f = True
        while len(q)>0 and f:
            n = len(q)
            for i in range(n):
                temp = q.pop(0)
                if temp:
                    s.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
                else:
                    s.append('#')
            flag = False
            for j in range(len(q)): # 判断队列中是否还存在有效节点
                if q[j]:
                    flag = True
                    break
            f = flag
        return s

    def Deserialize(self, s):
        # print(s)
        if len(s) == 0:
            return None
        root = TreeNode(int(s[0]))
        q = []
        q.append(root)
        i = 1
        while i<len(s): # 每轮给节点添加左右孩子
            if i<len(s):
                if s[i] == '#':
                    left = None
                else:
                    left = TreeNode(int(s[i]))
                    q.append(left)
                q[0].left = left
            if i+1<len(s):
                if s[i+1] == '#':
                    right = None
                else:
                    right = TreeNode(int(s[i+1]))
                    q.append(right)
                q[0].right = right
            q.pop(0)
            i += 2
        return root
