#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self , s: str) -> bool:
        if not s:
            return True
        if len(s)%2 != 0:
            return False
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False
        return True
