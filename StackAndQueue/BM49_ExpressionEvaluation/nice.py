# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
class Solution:
    def solve(self , s: str) -> int:
        s = s.strip()
        stack = [] # 辅助栈：用来存放待累加的元素
        res = 0 # 最后的结果
        num = 0 # 当前计算数
        sign = '+' # 当前运算符
        index = 0 # 遍历字符串的索引
        while index<len(s):
            if s[index] == ' ': # 跳过所有无效的空格符
                index += 1
                continue
            if s[index] == '(': # 括号内仍有可能继续嵌套括号！关键：找到与当前括号匹配的右括号！！
                end = index + 1
                lens = 1
                while lens>0:
                    if s[end] == '(':
                        lens += 1
                    if s[end] == ')':
                        lens -= 1
                    end += 1
                num = self.solve(s[index+1:end-1])
                index = end-1 # 重点！！！不能直接跳过')'，否则当子表达式处在末尾时，计算结果num不能参与运算！！！
                continue
            if '0' <= s[index] <= '9':
                num = num*10 + int(s[index]) # 数值有可能不是个位数！！！
            if not '0' <= s[index] <= '9' or index == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-1*num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                num = 0
                sign = s[index]
            index += 1
        while stack:
            res += stack.pop()
        return res
