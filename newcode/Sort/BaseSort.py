"""
基数排序
"""
class CountingSort:
    def countingSort(self, A, n):
        # write code here
        maxA, minA = max(A), min(A)
        hash = [0] * (maxA - minA + 1)
        for num in A:
            hash[num - minA] += 1
        A = []
        for i, v in enumerate(hash):
            A += [i+minA] * v
        return A

cs = CountingSort()
A = [1,2,3,5,2,3]

print(cs.countingSort(A, 6))