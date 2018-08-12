def bubbleSort(alist):
    for i in range(len(alist)-1):
        for j in range(1, len(alist)-i):
            if alist[j] < alist[j-1]:
                alist[j], alist[j - 1] = alist[j-1], alist[j]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

#短冒泡排序
# 冒泡排序通常被认为是最低效的排序方法，因为它必须在最终位置被知道之前交换项。 这些“浪费”的交换操作是非常昂贵的。
# 然而，因为冒泡排序遍历列表的整个未排序部分，它有能力做大多数排序算法不能做的事情。
# 特别地，如果在遍历期间没有交换，则我们知道该列表已排序。 如果发现列表已排序，可以修改冒泡排序提前停止。
# 这意味着对于只需要遍历几次列表，冒泡排序具有识别排序列表和停止的优点。 ActiveCode 2 展示了这种修改，通常称为 短冒泡排序。
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)