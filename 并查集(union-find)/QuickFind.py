"""
实现UnionFind算法。s使用最简单的quick-find方法
union(p, q)
find(p)
connected(p, q)
"""
class QuickFind():
    def __init__(self, N):
        self.id = [i for i in range(N)]     # 触点的类别
        self.count = N                      # 连通域个数

    def findID(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pID = self.id[p]
        qID = self.id[q]
        if pID == qID:
            return 0
        for i in range(len(self.id)):
            # 将p的分量命名为q的分量名称
            if self.id[i] == pID:
                self.id[i] = qID
        self.count -= 1

