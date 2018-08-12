#复杂度：O(n*n)
def insertionSort(alist):
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentValue

def insertSort(alist):
    for i in range(1, len(alist)):
        position = i
        for j in range(i):
            if alist[j] > alist[position]:
                alist[j], alist[position] = alist[position], alist[j]
                break
    return alist

alist = [54,26,93,17,77,31,44,55,20]
insertSort(alist)
print(alist)