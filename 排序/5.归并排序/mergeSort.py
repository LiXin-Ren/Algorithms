#先从询问基本情况开始，如果列表长度<=1，那么已经有有序的列表，并不需要更多的处理，
#如果长度大于1，使用python切片来提取左右两半。
#O(nlogn) 底数为2
'''
def mergeSort(alist):
    print("Splitting", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                alist[k] = leftHalf[i]
                i += 1
            else:
                alist[k] = rightHalf[j]
                j += 1
            k+=1

        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j += 1
            k += 1
    print("Merging", alist)
'''

def mergeSort(alist):
    if len(alist) > 1:
        midPosition = len(alist) // 2
        left = alist[:midPosition]
        right = alist[midPosition:]

        mergeSort(left)
        mergeSort(right)
        i = 0             # 左列表的索引
        j = 0               # 右列表的索引
        k = 0  # 合并列表的索引
        while i < len(left) and j < len(right):
            if left[i] < right[j]:  # 在right和left中选出最小的放在alist上。因为right和left都是排好序的，因此只需要在他们各自最低位中找。
                alist[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                alist[k] = right[j]
                j += 1
            k += 1
        while i < len(left):  # left中还有剩余
            alist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):  # right中还有剩余
            alist[k] = right[j]
            j += 1
            k += 1
        return alist



alist = [54,3,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)



















