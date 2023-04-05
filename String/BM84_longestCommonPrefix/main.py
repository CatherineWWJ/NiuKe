# @param strs string字符串一维数组
# @return string字符串
#
class Solution:
    def longestCommonPrefix(self , strs: List[str]) -> str:
        if not strs:
            return ""
        minLen = (len(strs[0]), 0) # 记录最小长度的字符串及其索引
        for i in range(1, len(strs)):
            minLen = (len(strs[i]), i) if len(strs[i]) < minLen[0] else minLen
        for i in range(minLen[0]):
            tag = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != tag:
                    return strs[j][:i]
        return strs[minLen[1]]
