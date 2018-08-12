def selectionSort(alist):
    for i in range(len(alist) - 1):
        positionOfMax = 0
        for j in range(1, len(alist) - i):
            if alist[j] > alist[positionOfMax]:
                positionOfMax = j
        alist[positionOfMax], alist[len(alist) - i - 1] = alist[len(alist) - i - 1], alist[positionOfMax]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)