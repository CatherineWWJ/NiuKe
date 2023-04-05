# @param str string字符串 待判断的字符串
# @return bool布尔型
#
class Solution:
    def judge(self , str: str) -> bool:
        if not str or len(str) < 2:
            return True
        l = 0
        r = len(str)-1
        while l<r:
            if str[l] != str[r]:
                return False
            l += 1
            r -= 1
        return True
    