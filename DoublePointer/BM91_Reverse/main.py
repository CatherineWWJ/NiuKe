# 反转字符串
# @param str string字符串
# @return string字符串
#
class Solution:
    def solve(self, str: str) -> str:
        if not str or len(str) < 2:
            return str
        result = ""
        for i in range(len(str) - 1, -1, -1):
            result += str[i]
        return result
