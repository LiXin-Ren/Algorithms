import QuickUnion
import QuickFind
import WeightQuickUnion

#qf1 = QuickFind.QuickFind(10)
# final id list is 1,1,1,8,8,1,1,1,8,8
# count of components is: 2

#qf = QuickUnion.QuickUnion(10)
# final root list is 1,1,1,8,3,0,5,1,8,8
# count of components is: 2

qf = WeightQuickUnion.WeightQuickUnion(10)
# final id list is 6,2,6,4,4,6,6,2,4,4
# count of components is: 2
print("initial id list is %s" % (",").join(str(x) for x in qf.id))
list = [
    (4, 3),
    (3, 8),
    (6, 5),
    (9, 4),
    (2, 1),
    (8, 9),
    (5, 0),
    (7, 2),
    (6, 1),
    (1, 0),
    (6, 7)
]

for k in list:
    p = k[0]
    q = k[1]
    qf.union(p, q)
    print("%d and %d is connected? %s" % (p, q, str(qf.connected(p, q))))

print("final id list is %s" % (",").join(str(x) for x in qf.id))
print("count of components is: %d" % qf.count)


