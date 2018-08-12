# class BinHeap:
#     def __init__(self):
#         self.heapList = [0]
#         self.currentSize = 0
#
#     def percUp(self, index):
#         while index // 2 > 0 and self.heapList[index//2] > self.heapList[index]:
#             self.heapList[index//2], self.heapList[index] = self.heapList[index], self.heapList[index//2]
#             index = index // 2
#
#     def insert(self, k):
#         self.heapList.append(k)
#         self.currentSize += 1
#         self.percUp(self.currentSize)
#
#     def minChild(self, i):
#         if i * 2 + 1 > self.currentSize:
#             return 2 * i
#
#         return 2*i if (self.heapList[2*i] < self.heapList[2*i + 1]) else 2*i+1
#
#     def percDown(self, index):
#         while index * 2 <= self.currentSize:
#             mc = self.minChild(index)
#             if self.heapList[index] > self.heapList[mc]:
#                 self.heapList[index], self.heapList[mc] = self.heapList[mc], self.heapList[index]
#             index = mc
#
#     def delMin(self):
#         res = self.heapList[1]
#         self.heapList[1] = self.heapList[-1]
#         self.heapList.pop()
#         self.currentSize -= 1
#         self.percDown(1)
#         return res
#
#     def buildHeap(self, alist):
#         self.currentSize = len(alist)
#         self.heapList = [0] + alist
#         i = self.currentSize // 2
#         while i > 0:
#             self.percDown(i)
#             i -= 1
# bh = BinHeap()
# bh.buildHeap([9,5,6,2,3])
#
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())

def heapSort(alist):
    def maxChild(i, end):
        if i * 2 + 1 > len(alist) or i*2+1>end:
            return 2 * i
        return 2 * i if (alist[2 * i] < alist[2 * i + 1]) else 2 * i + 1

    def percDown(start, end):
        while start * 2 <= end:
            mc = maxChild(start, end)
            if alist[start] > alist[mc]:
                alist[start], alist[mc] = alist[mc], alist[start]
            start = mc


    def buildHeap(alist):
        i = len(alist) // 2
        alist.insert(0, 0)
        while i > 0:
            percDown(i, len(alist) - 1)
            i -= 1

    buildHeap(alist)  # 构建最大堆
    for i in range(len(alist)-1, 1, -1):
        alist[i], alist[1] = alist[1], alist[i]
        percDown(1, i-1)
    return alist[1:]



print(heapSort([6, 5, 9, 7, 3, 19, 0, 7, 2]))










