# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
class Solution:
    def merge(self , A, m, B, n):
        k = m+n-1
        i = m-1
        j = n-1
        while i>=0 and j>=0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        while j>=0:
            A[k] = B[j]
            j -= 1
            k -= 1
