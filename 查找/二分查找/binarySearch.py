def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while not found and last >= first:
        mid = (last + first) // 2
        if item == alist[mid]:
            found = True
        else:
            if item > alist[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return found


#递归版本
def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False

    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item > alist[mid]:
                return binarySearchRecursive(alist[mid + 1:], item)
            else:
                return binarySearchRecursive(alist[:mid], item)


# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 13))

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearchRecursive(testlist, 3))
print(binarySearchRecursive(testlist, 13))