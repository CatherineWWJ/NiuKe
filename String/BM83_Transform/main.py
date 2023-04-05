# @param s string字符串
# @param n int整型
# @return string字符串
#
class Solution:
    def trans(self , s: str, n: int) -> str:
        arr = s.split(" ")
        for i in range(len(arr)-1, -1, -1):
            arr[i] = arr[i].swapcase()
        arr.reverse()
        result = " ".join(arr)
        return result
    