# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
    def push(self, node):
        if not self.stack:
            self.stack.append((node, node)) # 元组（数值，栈内最小值）
        else:
            self.stack.append((node, min(node, self.stack[-1][1]))) # 栈内最小值一定是先于node入栈！！！
    def pop(self):
        if not self.stack:
            return -1
        else:
            return self.stack.pop()
    def top(self):
        if not self.stack:
            return -1
        else:
            return self.stack[-1][0]
    def min(self):
        return self.stack[-1][1]
    