"""
8.25 头条笔试
团队里一共有n个人，每个人提供了自己认识的人的名字，不包括自己。
如果A的名单里有B, 或者B的名单里有A，则代表A与B互相认识，同时如果A认识B，B认识C，那么A与C也会认识。

字节君根据名单将团队氛围m组，每组人数可以不同，但组内的任何一个人都与组内其他所有人直接或间接的认识。
如何确定一个方案，使得团队可以分成m组，并且这个m尽可能小

10
0
5 3 0
8 4 0
9 0
9 0
3 0
0
7 9 0
0
9 7 0

输出：2
"""
import WeightQuickUnion
import QuickUnion
import QuickFind
n = int(input())

wqu = WeightQuickUnion.WeightQuickUnion(n)
#wqu = QuickUnion.QuickUnion(n)
#wqu = QuickFind.QuickFind(n)
for i in range(n):
    line = list(map(int, input().split()))
    for num in line:
        if num != 0:
            wqu.union(i, num-1)

print(wqu.count)
#print("id: ", wqu.id)