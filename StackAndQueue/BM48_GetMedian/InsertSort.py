class Solution:
    def __init__(self):
        self.arr = []

    def Insert(self, num):
        self.arr.append(num)
        for j in range(len(self.arr) - 1, 0, -1):
            if self.arr[j] < self.arr[j - 1]:
                self.arr[j], self.arr[j - 1] = self.arr[j - 1], self.arr[j]
            else:
                break

    def GetMedian(self):
        n = len(self.arr)
        if n % 2 == 0:
            return (self.arr[n // 2] + self.arr[n // 2 - 1]) / 2
        else:
            return self.arr[n // 2]