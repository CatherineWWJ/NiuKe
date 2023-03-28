# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        while len(self.stack2)>0: # 不要再把while写成if啦！！！
            self.stack1.append(self.stack2.pop())
        self.stack1.append(node)
    def pop(self):
        while len(self.stack1)>0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
