"""
quick-union方法实现:
改进：在前一个算法的基础上提高了union的速度，不再通过遍历list来修改连通id，而是通过一种“链接”的方式
找到根节点。当id[p] = p时，说明p是一个根节点
和使用路径压缩的加权quick-union
"""

class QuickUnion():
    def __init__(self, N):
        self.count = N
        self.id = [i for i in range(N)]

    def connected(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def findRoot(self, p):
        # 找出p的分量名称
        while self.id[p] != p:
            p = self.id[p]
        return p

    def union(self, p, q):
        pRoot = self.findRoot(p)
        qRoot = self.findRoot(q)
        if not self.connected(p, q):
            self.id[pRoot] = qRoot
            self.count -= 1