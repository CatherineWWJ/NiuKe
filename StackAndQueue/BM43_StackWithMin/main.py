# -*- coding:utf-8 -*-
class Solution:
    stack = []
    def push(self, node):
        self.stack.append(node)
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        return self.stack.pop()
    def top(self):
        if len(self.stack) <= 0:
            return -1
        return self.stack[len(self.stack)-1] # 优化：栈顶元素（索引值为-1）
    def min(self):
        if len(self.stack) <= 0:
            return -1
        min = self.stack[0]
        for i in range(1,len(self.stack)):
            if self.stack[i] < min:
                min = self.stack[i]
        return min
    