# 比较版本号
# @param version1 string字符串
# @param version2 string字符串
# @return int整型
#
class Solution:
    def compare(self , version1: str, version2: str) -> int:
        m = len(version1)
        n = len(version2)
        l1, l2, r1, r2 = 0,0,0,0
        while r1<m and r2<n:
            while l1<m and version1[l1] == '0':
                l1 += 1
            r1 = l1
            while r1<m and version1[r1] != '.':
                r1 += 1
            while l2<n and version2[l2] == '0':
                l2 += 1
            r2 = l2
            while r2<n and version2[r2] != '.':
                r2 += 1
            if r1-l1 > r2-l2: # 比较字符串的长度即所代表的数字的位数
                return 1
            elif r1-l1 < r2-l2:
                return -1
            else:
                for k in range(r1-l1):
                    if version1[l1+k] < version2[l2+k]:
                        return -1
                    elif version1[l1+k] > version2[l2+k]:
                        return 1
            l1 = r1+1
            r1 = l1
            l2 = r2+1
            r2 = l2
        if l1>m-1 and l2<n: # version1短 version2长（判断较长版本号后是否存在有效数字）
            for k in range(l2,n):
                if version2[k] == '0' or version2[k] == '.':
                    continue
                else:
                    return -1
            return 0
        if l1<m and l2>n-1: # version1长 version2短
            for k in range(l1,m):
                if version1[k] == '0' or version1[k] == '.':
                    continue
                else:
                    return 1
            return 0
        return 0
