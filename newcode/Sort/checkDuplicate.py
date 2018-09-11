"""
请设计一个高效算法，判断数组中是否有重复值。必须保证额外空间复杂度为O(1)。

给定一个int数组A及它的大小n，请返回它是否有重复值。

测试样例：
[1,2,3,4,5,5,6],7
返回：true

使用堆排序
"""

def heapSort(A, n):

    def checkDuplicate(self, a, n):
        # write code here
        def build

    def maxChild(start, end):
        if start*2+1<=end and A[end] > A[end-1]:
            return end
        return end-1


    def percDown(start, end):
        while start*2 < end:
            mc = maxChild(start, end)
            if A[mc] > A[start]:
                A[mc], A[start] = A[start], A[mc]
            start += 1



    def buildHeap(A, n):    #构建最大堆
        i = n//2
        A.insert(0,0)
        while i > 0:
            percDown(A, i, len(A) - 1)
        for
A = list(map(int, input().split()))
heapA = buildHeap(A, n)

