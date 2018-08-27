"""
加权quick-union
改进：
不是随意将一棵树连接到另一颗树，而是记录每棵数的大小并总是把较小的树连接到较大的树上。
"""
class WeightQuickUnion():
    def __init__(self, N):
        self.count = N
        self.id = [i for i in range(N)]
        self.treeSize = [1 for i in range(N)]

    def findRoot(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def union(self, p, q):
        pRoot = self.findRoot(p)
        qRoot = self.findRoot(q)

        if not self.connected(p, q):
            if self.treeSize[p] < self.treeSize[q]:
                self.id[pRoot] = qRoot
                self.treeSize[qRoot] += self.treeSize[pRoot]
            else:
                self.id[qRoot] = pRoot
                self.treeSize[pRoot] += self.treeSize[qRoot]
            self.count -= 1


