def shellSort(alist):
    subListCount = len(alist)//2

    while subListCount > 0:
        for i in range(subListCount):
            gapInsertSort(alist, i, subListCount)

        subListCount //= 2

def gapInsertSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position >= gap and currentValue < alist[position - gap]:
            alist[i] = alist[position - gap]
            position = position - gap

        alist[position] = currentValue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)




















