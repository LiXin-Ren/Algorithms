def quickSort(alist):
    quickSortCore(alist, 0, len(alist) - 1)

def quickSortCore(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)

        quickSortCore(alist, first, splitPoint-1)
        quickSortCore(alist, splitPoint + 1, last)


def partition(alist, first, last):
    pivotValue = alist[first]

    leftMark = first + 1
    rightMark = last

    while leftMark < rightMark:
        while alist[leftMark] < pivotValue:
            leftMark += 1
        while alist[rightMark] > pivotValue:
            rightMark -= 1

        if leftMark < rightMark:
            alist[leftMark], alist[rightMark] = alist[rightMark], alist[leftMark]
            rightMark -= 1
            leftMark += 1

    alist[rightMark], alist[first] = alist[first], alist[rightMark]

    return rightMark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)